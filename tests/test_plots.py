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

from seaborn_qqplot.plots import (
    _Plot,
    PPPlot,
    ProbabilityPlot,
    QQPlot,
    QuantilePlot
)


class TestEmptyPlot(unittest.TestCase):

    def setUp(self):        
       self.empty_plot = _Plot()

    def test_empty_variables(self):
        self.assertEqual(self.empty_plot.identity, False)
        self.assertEqual(self.empty_plot.fit, False)
        self.assertEqual(self.empty_plot.reg, False)
        self.assertEqual(self.empty_plot.ci, 0.05)


class TestPlot(unittest.TestCase):

    def setUp(self):        
       self.plot = _Plot(**{
           'display_kws':{
            'identity':True,
            'fit':True,
            'reg':True,
            'ci':0.01
        }
       })

    def test_variables(self):
        self.assertEqual(self.plot.identity, True)
        self.assertEqual(self.plot.fit, True)
        self.assertEqual(self.plot.reg, True)
        self.assertEqual(self.plot.ci, 0.01)


class TestPPPlots(unittest.TestCase):

    def setUp(self):        
        self.ppplot = PPPlot()


    def test_range(self):
        x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.ppplot(x,x)
        xr, yr = self.ppplot._get_axis_data(x,x)

        result = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
        0.1111111111111111, 0.1111111111111111, 0.1111111111111111, 0.1111111111111111, 0.1111111111111111, 0.1111111111111111, 0.1111111111111111, 0.1111111111111111, 0.1111111111111111, 0.1111111111111111, 
        0.2222222222222222, 0.2222222222222222, 0.2222222222222222, 0.2222222222222222, 0.2222222222222222, 0.2222222222222222, 0.2222222222222222, 0.2222222222222222, 0.2222222222222222, 0.2222222222222222, 
        0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333,
        0.4444444444444444, 0.4444444444444444, 0.4444444444444444, 0.4444444444444444, 0.4444444444444444, 0.4444444444444444, 0.4444444444444444, 0.4444444444444444, 0.4444444444444444, 0.4444444444444444,
        0.5555555555555556, 0.5555555555555556, 0.5555555555555556, 0.5555555555555556, 0.5555555555555556, 0.5555555555555556, 0.5555555555555556, 0.5555555555555556, 0.5555555555555556, 0.5555555555555556,
        0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666,
        0.7777777777777777, 0.7777777777777777, 0.7777777777777777, 0.7777777777777777, 0.7777777777777777, 0.7777777777777777, 0.7777777777777777, 0.7777777777777777, 0.7777777777777777, 0.7777777777777777,
        0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888,
        1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

        npt.assert_almost_equal(xr, result)
        npt.assert_almost_equal(yr, result)



class TestQQPlots(unittest.TestCase):

    def setUp(self):        
        self.qqplot = QQPlot()


    def test_range(self):
        x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.qqplot(x,x)
        xr, yr = self.qqplot._get_axis_data(x,x)
        data = [ 6. ,  6.9,  7.8,  8.7,  9.6, 10.5, 11.4, 12.3, 13.2, 14.1]

        npt.assert_almost_equal(xr, data)
        npt.assert_almost_equal(yr, data)


class TestQPlots(unittest.TestCase):

    def setUp(self):        
        self.qplot = QuantilePlot()


    def test_range(self):
        x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.qplot(x,x)
        _, yr = self.qplot._get_axis_data(x,x)
        data = [ 6. ,  6.9,  7.8,  8.7,  9.6, 10.5, 11.4, 12.3, 13.2, 14.1]

        npt.assert_almost_equal(yr, data)
