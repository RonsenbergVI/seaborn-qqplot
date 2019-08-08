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

from scipy.stats import probplot, linregress, t

import numpy as np

def probability_plot(x, y, **kwargs):
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
    display_kws = kwargs["display_kws"]
    plot_kws = kwargs["plot_kws"]

    identity = False
    fit = False
    reg = False
    ci = 0.05

    # extracing key words arguments needed for displaying qqplot
    if display_kws is not None:
        if 'identity' in display_kws.keys():
            identity = display_kws['identity']

        if 'fit' in display_kws.keys():
            fit = display_kws['fit']

        if 'reg' in display_kws.keys():
            reg = display_kws['reg']

        if 'ci' in display_kws.keys():
            ci = display_kws['ci']

    # get qqplot data
    _, xr = probplot(x, fit=False)
    _, yr = probplot(y, fit=False)

    # display regression
    if fit:
        slope, intercept, *_ = linregress(xr,yr)
        plt.plot(xr, intercept + slope * xr, color=kwargs['color'], **plot_kws)

        if reg:
            # confidence intervals
            p = 1 - ci/2
            y_model = intercept + slope * xr
            N = xr.size
            df = N - 2
            q_t = t.ppf(p, df)
            s_err = np.sqrt(np.sum((y - y_model)**2)/(df))
            x2 = np.linspace(np.min(xr), np.max(xr), 100)
            y2 = intercept + slope * x2
            c = q_t * s_err * np.sqrt(1/N + (x2-np.mean(x))**2/np.sum((x-np.mean(x))**2))
            plt.gca().fill_between(x2, y2+c, y2-c, color=kwargs['color'], alpha=0.1, **plot_kws)

    # qqplot
    plt.scatter(xr, yr, color=kwargs['color'], **plot_kws)

    # identity line in plot
    if identity:
        plt.plot(yr,yr, color='black', **plot_kws)

    return plt.axes
