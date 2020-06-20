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

import numpy as np
from scipy.stats import probplot, linregress, t


class TransformMixin:
    """
    Transforms are objects that perform transformation on data.
    Such as scaling, centering, quantile transformation
    """

    def __call__(self, x, y=None, **kwargs):
        raise NotImplementedError("Transformer must be callable")


class IdentityTransform(TransformMixin):
    """
    Identity transform.
    """

    def __call__(self, x, y=None, **kwargs):
        if y:
            return x, y
        return x


class RegressionFit(TransformMixin):
    """
    Returns regression line.
    """

    def __call__(self, x, y=None, **kwargs):
        slope, intercept, *_ = linregress(x,y)
        return x, intercept + slope * x


class ConfidenceInterval(TransformMixin):
    """
    Returns confidence interval
    """

    def __init__(self, ci=0.05):
        self.p = 1 - ci/2

    def __call__(self, x, y=None, **kwargs):
        _, y1   = RegressionFit()(x,y)
        N       = x.size
        x2      = np.linspace(np.min(x), np.max(x), N)
        _, y2   = RegressionFit()(x2,y)
        df      = N - 2
        q_t     = t.ppf(self.p, df)
        s_err   = np.sqrt(np.sum((y - y1)**2)/(df))
        c       = q_t * s_err * np.sqrt(1/N + (x2-np.mean(x))**2/np.sum((x-np.mean(x))**2))
        return x2, y2 + c, y2 - c


class Scale(TransformMixin):

    def __init__(self, scale='linear'):
        if scale == 'log':
            self.scale = np.log
        else:
            self.scale = None

    def __call__(self, x, y=None, **kwargs):
        if self.scale:
            return np.apply_along_axis(self.scale, 0, x)
        return x


class EmpiricalCDF(TransformMixin):

    def __call__(self, x):
        """ Compute ECDF """
        x_sorted = np.sort(x)
        n = x_sorted.size
        y = np.arange(1, n+1) / n
        return x_sorted, y


class EmpiricalQuantilesFunction(TransformMixin):

    def __init__(self, interpolation='linear'):
        self.interpolation = interpolation

    def __call__(self, x, y=None, **kwargs):
        quantiles = np.linspace(start=0, stop=1, num=len(x))
        xr = np.quantile(x, quantiles, interpolation=self.interpolation)
        return xr, quantiles
