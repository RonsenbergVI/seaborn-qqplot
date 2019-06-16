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

import os
import sys
from setuptools import setup, find_packages
from distutils.sysconfig import get_python_lib
from configparser import ConfigParser

config_file = os.path.join(os.path.dirname(__file__), 'setup.cfg')

if "install" in sys.argv:
    lib_paths = [get_python_lib()]
    if lib_paths[0].startswith("/usr/lib/"):
        lib_paths.append(get_python_lib(prefix="/usr/local"))
    for lib_path in lib_paths:
        existing_path = os.path.abspath(os.path.join(lib_path, "seaborn_qqplot"))

def get_version_info():
	"""
	get_version_info
	------------
	gets software version infos from
	"""
	config=ConfigParser()
	config.read(config_file)
	MAJOR=config['version']['major']
	MINOR=config['version']['minor']
	MICRO=config['version']['micro']

	ISRELEASED = True

	VERSION = '%s.%s.%s' % (MAJOR, MINOR, MICRO)

	return VERSION, ISRELEASED

def write_version_py(filename="version.py"):
	"""
	write_version_py
	------------
	write software version infos in version.py file
	"""
	file_content = """
# FILE CONTENT GENERATED FROM SETUP.PY
short_version = '%(version)s'
version = '%(version)s'
full_version = '%(full_version)s'
release = %(isrelease)s

if not release:
       version = full_version
	"""

	filename = os.path.join(os.path.dirname(__file__), 'seaborn_qqplot/%s' % filename)

	VERSION, ISRELEASED = get_version_info()

	_file = open(filename,'w+')

	try:
		_file.write(file_content % {'version': VERSION,
                       'full_version' : VERSION,
                       'isrelease': str(ISRELEASED)})
	finally:
		_file.close()

def setup_package():

    _version, _isReleased = get_version_info()

    write_version_py()

    setup(name = 'seaborn-qqplot',
          version = str(_version),
          description = 'qqplots for seaborn',
          author = 'Rene-Jean Corneille',
          author_email = 'rene_jean.corneille@edu.escpeurope.eu',
          license = 'MIT',
          keywords = ['quantile', 'qq-plot', 'plot', 'e', 'filter', 'trading', 'stocks', 'equities', 'forex'],
          url = 'https://github.com/RonsenbergVI/seaborn-qqplot',
          zip_safe = False,
          include_package_data = True,
          platforms = 'any',
		  packages=['seaborn_qqplot'],
          install_requires = ['scipy',
                              'pandas',
                              'seaborn',
							  'tabulate'],
          classifiers = [
            'Development Status :: 3 - Alpha',
            'Environment :: Web Environment',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Topic :: Scientific/Engineering :: Mathematics',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ])

if __name__ == "__main__":
    setup_package()
