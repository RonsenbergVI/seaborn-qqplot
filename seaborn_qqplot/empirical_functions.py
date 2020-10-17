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
from scipy.interpolate import interp1d

# from statmodels.distributions.empirical_distributions
class StepFunction:
    """
    A basic step function.
    Values at the ends are handled in the simplest way possible:
    everything to the left of x[0] is set to ival; everything
    to the right of x[-1] is set to y[-1].
    Parameters
    ----------
    x : array_like
    y : array_like
    ival : float
        ival is the value given to the values to the left of x[0]. Default
        is 0.
    sorted : bool
        Default is False.
    side : {'left', 'right'}, optional
        Default is 'left'. Defines the shape of the intervals constituting the
        steps. 'right' correspond to [a, b) intervals and 'left' to (a, b].
    """

    def __init__(self, x, y, ival=0., sorted=False, side='left'):

        if side.lower() not in ['right', 'left']:
            msg = "side can take the values 'right' or 'left'"
            raise ValueError(msg)
        self.side = side

        _x = np.asarray(x)
        _y = np.asarray(y)

        if _x.shape != _y.shape:
            msg = "x and y do not have the same shape"
            raise ValueError(msg)
        if len(_x.shape) != 1:
            msg = 'x and y must be 1-dimensional'
            raise ValueError(msg)

        self.x = np.r_[-np.inf, _x]
        self.y = np.r_[ival, _y]

        if not sorted:
            asort = np.argsort(self.x)
            self.x = np.take(self.x, asort, 0)
            self.y = np.take(self.y, asort, 0)
        self.n = self.x.shape[0]

    def __call__(self, x):
        """
        """
        tind = np.searchsorted(self.x, x, self.side) - 1
        return self.y[tind]


class EmpiricalCDF(StepFunction):
    """
    Return the Empirical CDF of an array as a step function.
    Parameters
    ----------
    x : array_like
        Observations
    side : {'left', 'right'}, optional
        Default is 'right'. Defines the shape of the intervals constituting the
        steps. 'right' correspond to [a, b) intervals and 'left' to (a, b].
    Returns
    -------
    Empirical CDF as a step function.
    """
    def __init__(self, x, side='right'):
        x = np.array(x, copy=True)
        x.sort()
        nobs = len(x)
        y = np.linspace(0,1,nobs)
        super(EmpiricalCDF, self).__init__(x, y, side=side, sorted=True)
        # TODO: make `step` an arg and have a linear interpolation option?
        # This is the path with `step` is True
        # If `step` is False, a previous version of the code read
        #  `return interp1d(x,y,drop_errors=False,fill_values=ival)`
        # which would have raised a NameError if hit, so would need to be
        # fixed.  See GH#5701.


def monotone_fn_inverter(fn, x, vectorized=True, **kwargs):
    """
    Given a monotone function fn (no checking is done to verify monotonicity)
    and a set of x values, return an linearly interpolated approximation
    to its inverse from its values on x.
    """
    x = np.asarray(x)
    if vectorized:
        y = fn(x, **kwargs)
    else:
        y = []
        for _x in x:
            y.append(fn(_x, **kwargs))
        y = np.array(y)

    a = np.argsort(y)

    return interp1d(y[a], x[a])


class EmpiricalQF(EmpiricalCDF):

    def __call__(self, x):
        """
        The quantile function can be defined as the inverse cdf.
        https://en.wikipedia.org/wiki/Quantile_function
        """
        return monotone_fn_inverter(super(EmpiricalCDF, self).__call__, self.x)(x)
