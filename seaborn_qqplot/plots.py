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

import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import rv_continuous, probplot, linregress, t

from seaborn_qqplot.transform import (
    RegressionFit,
    ConfidenceInterval,
    Scale,
    EmpiricalCDF,
    EmpiricalQuantilesFunction,
)


class _Plot:

    def __init__(self, **kwargs):

        display_kws = kwargs.pop("display_kws", {})
        self.plot_kws = kwargs.pop("plot_kws", {})

        self.identity    = display_kws.get('identity', False)
        self.fit         = display_kws.get('fit', False)
        self.reg         = display_kws.get('reg', False)
        self.ci          = display_kws.get('ci', 0.05)
    
    def _get_axis_data(self, x, y):
        raise NotImplementedError("")        

    def __call__(self, x, y, **kwargs):
        """ Draw a probability plot of data contained in x against data in y.

        Parameters
        ----------
        x : array_like
            Data
        y : array_like
            Data
        kwargs : key, value pairings
            Additional keyword arguments are passed to the function.
        """

        xr, yr = self._get_axis_data(x,y)

        # display regression
        if self.fit:
            regression = RegressionFit()
            xr, yr = regression(xr,yr)
            plt.plot(xr, yr, **self.plot_kws)

            if self.reg:
                # confidence intervals
                confidence_interval = ConfidenceInterval(ci=self.ci)
                a,b,c= confidence_interval(x,y)
                plt.gca().fill_between(a, b, c, color=kwargs['color'], alpha=0.1, **self.plot_kws)


        plt.scatter(xr, yr, color=kwargs['color'], **self.plot_kws)

        if self.identity:
            plt.plot(yr,yr, color='black', **self.plot_kws)

        return plt.axes



class ProbabilityPlot(_Plot):

    def _get_axis_data(self, x, y):
        _, xr = probplot(x, fit=False)
        _, yr = probplot(y, fit=False)
        return xr, yr

class QuantilePlot(_Plot):

    def _get_axis_data(self, x, y):
        _, xr = probplot(x, fit=False)
        _, yr = probplot(y, fit=False)
        return xr, yr


class QQPlot(_Plot):

    def _get_axis_data(self, x, y):
        _, xr = probplot(x, fit=False)
        _, yr = probplot(y, fit=False)
        return xr, yr

class PPPlot(_Plot):

    def _get_axis_data(self, x, y):
        _, xr = probplot(x, fit=False)
        _, yr = probplot(y, fit=False)
        return xr, yr
