
# BSD 3-Clause License
#
# Copyright (c) 2019, Rene Jean Corneille
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
Release script widely inspired from flask_mail
"""

import sys
import os
import re

from datetime import datetime, date
from subprocess import Popen, PIPE
from configparser import ConfigParser

def installed_list():
	libs_list = Popen(['pip', 'freeze'], stdout=PIPE).communicate()[0].decode("utf-8").split("\r\n")
	return {str(lib.split("==")[0]).lower() : lib.split("==")[1] for lib in libs_list[:-1]}

def is_installed(lib):
	return lib in installed_list().keys()

def get_changes():
    with open('CHANGES','r+') as file:
        for line in iter(file):
            match = re.search('Version\s+(.*)', line.strip())

            if match is None:
                continue

            version = match.group(1).strip()

            if next(file).count('-') != len(line.strip()):
                print_error('Invalid hyphen count below version line: %s', line.strip())

            while 1:
                released = next(file).strip()
                if released:
                    break

            match = re.search(r'Release day: (\w+\s+\d+\w+\s+\d+)', released)

            if match is None:
                print_error('Could not find release date in version %s' % version)

            release_day = get_date(match.group(1).strip())

            return version, release_day

def get_date(string_date):
    string_date = re.compile(r'(\d+)(st|nd|rd|th)').sub(r'\1', string_date)
    return datetime.strptime(string_date, '%B %d %Y')

def print_error(message, *args):
    print('Error: %s' % (message % args))
    sys.exit(1)

def print_info(message, *args):
	print(message % args)

def get_version(version_string):
	try:
		parts = list(map(int, version.split('.')))
		MAJOR=parts[0]
		MINOR=parts[1]
		MICRO=parts[2]
	except ValueError:
		print_error('Current version is not numeric')
	return MAJOR, MINOR, MICRO

def write_new_version(major,minor,micro,release=""):
	filename = 'setup.cfg'
	config = ConfigParser()
	config.read(filename)
	config['version']['major'] = major
	config['version']['minor'] = minor
	config['version']['micro'] = micro
	with open(filename, 'w') as configfile:
		config.write(configfile)
		configfile.close()
	print_info("Current version is now: %s.%s.%s" % (major, minor, micro))

def build_for_release():
	Popen([sys.executable, 'setup.py','sdist','--formats=gztar,zip','register','upload']).wait()

if __name__ == '__main__':
	version, day = get_changes()
	major,minor,micro = get_version(version)
	write_new_version(str(major),str(minor),str(micro))
	build_for_release()
