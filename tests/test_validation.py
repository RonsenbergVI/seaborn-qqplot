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

import unittest

from pandas import DataFrame

from seaborn_qqplot.validation import (
    _validate_data,
    _validate_x_and_y,
    _validate_interpolation,
    _validate_kind,
    _validate_argument
)

class TestTransform(unittest.TestCase):


    def test_validate_data_fails(self):
        data = DataFrame()
        self.assertEqual(_validate_data(data).values.tolist(), [])

    def test_validate_data(self):
        data = dict()
        with self.assertRaises(TypeError):
            _validate_data(data)
            
    def test_validate_x_and_y_fails(self):
        with self.assertRaises(TypeError):
            _validate_x_and_y(None, None)

    def test_validate_interpolation_fails(self):
        with self.assertRaises(ValueError):
            _validate_interpolation(25)

    def test_validate_kind_fails(self):
        with self.assertRaises(ValueError):
            _validate_kind('qqq')
        
    def test_validate_argument_fails(self):
        with self.assertRaises(ValueError):
            _validate_argument('a', 'test', ['b', 'c'])
        