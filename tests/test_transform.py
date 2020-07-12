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
from seaborn_qqplot.transforms import (
    TransformMixin,
    RegressionFit,
    ConfidenceInterval,
    Scale
)

class TestTransform(unittest.TestCase):

    def test_abstract_class(self):
        x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        with self.assertRaises(NotImplementedError):
            TransformMixin()(x)


    def test_regression(self):
        x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        r = RegressionFit(x,x)
        self.assertEqual(r.slope, 1.0)
        self.assertEqual(r.intercept, 0.0)

    def test_confidence_interval(self):
        x = [6., 7., 8., 9., 10., 11., 12., 13., 14., 15.]
        r = ConfidenceInterval(x,x)
        a,b,c = r(np.array(x),np.array(x))

        npt.assert_almost_equal(a, np.array(x))
        npt.assert_almost_equal(b, np.array(x))
        npt.assert_almost_equal(c, np.array(x))
        

    def test_scale(self):
        x = [6., 7., 8., 9., 10., 11., 12., 13., 14., 15.]
        scale = Scale(scale='log')
        y = scale(x)
        result = [1.79175947, 1.94591015, 2.07944154, 2.19722458, 2.30258509, 2.39789527,
            2.48490665, 2.56494936, 2.63905733, 2.7080502]
        npt.assert_almost_equal(y, result)

        scale = Scale(scale='linear')
        npt.assert_almost_equal(x, scale(x))