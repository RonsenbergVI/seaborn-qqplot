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

import numpy as np
import numpy.testing as npt
from numpy.testing import assert_raises

from seaborn_qqplot.empirical_functions import (
    StepFunction,
    monotone_fn_inverter,
    EmpiricalCDF,
    EmpiricalQF
)

# from seaborn_qqplot.distributions.tests
class TestDistributions(unittest.TestCase):

    def test_step_function(self):
        x = np.arange(20)
        y = np.arange(20)
        f = StepFunction(x, y)
        npt.assert_almost_equal(f( np.array([[3.2,4.5],[24,-3.1],[3.0, 4.0]])),
                                             [[ 3, 4], [19, 0],  [2, 3]])


    def test_step_function_bad_shape(self):
        x = np.arange(20)
        y = np.arange(21)
        with self.assertRaises(ValueError):
            StepFunction(x,y)
        x = np.zeros((2, 2))
        y = np.zeros((2, 2))
        with self.assertRaises(ValueError):
            StepFunction(x,y)


    def test_step_function_value_side_right(self):
        x = np.arange(20)
        y = np.arange(20)
        f = StepFunction(x, y, side='right')
        npt.assert_almost_equal(f( np.array([[3.2,4.5],[24,-3.1],[3.0, 4.0]])),
                                             [[ 3, 4], [19, 0],  [3, 4]])


    def test_step_function_repeated_values(self):
        x = [1, 1, 2, 2, 2, 3, 3, 3, 4, 5]
        y = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        f = StepFunction(x, y)
        npt.assert_almost_equal(f([1, 2, 3, 4, 5]), [0, 7, 10, 13, 14])
        f2 = StepFunction(x, y, side='right')
        npt.assert_almost_equal(f2([1, 2, 3, 4, 5]), [7, 10, 13, 14, 15])


    def test_monotone_fn_inverter(self):
        x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        fn = lambda x : 1./x
        y = fn(np.array(x))
        f = monotone_fn_inverter(fn, x)
        npt.assert_array_equal(f.y, x[::-1])
        npt.assert_array_equal(f.x, y[::-1])


    def test_ecdf(self):
        x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        ecdf = EmpiricalCDF(x)
        npt.assert_almost_equal(ecdf(x), [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.])


    def test_eqf(self):
        x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        eqf = EmpiricalQF(x)
        npt.assert_almost_equal(eqf([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.]), [6, 7, 8, 9, 10, 11, 12, 13, 14, 15])