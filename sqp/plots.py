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

from sqp import probability_plot

from seaborn import PairGrid

from scipy.stats import rv_continuous

def qq(data, x=None, y=None, hue = None, hue_order=None, palette = None, kind="quantile",
       height = 2.5, aspect = 1, dropna=True, display_kws=None, plot_kws=None):
    """
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError(
            "'data' must be pandas DataFrame object, not: {typefound}".format(
                typefound=type(data)))

    if x is None or y is None:
        raise TypeError()

    x_vars = [x]

    data_ = data.copy()

    if isinstance(y, rv_continuous):
        y_ = y(*y.fit(data_[x])).rvs(len(data_[x]))
        name = "{}_dist".format(y.name)
        data_[name] = pd.Series(y_, index=data_.index)
        y_vars=[name]
    else:
        y_vars = [y]

    if plot_kws is None:
        plot_kws = {}
    if display_kws is None:
        display_kws = {}

    kws = {"plot_kws":plot_kws, "display_kws":display_kws}

    grid = PairGrid(data_, x_vars=x_vars, y_vars=y_vars, height=height, aspect=aspect, hue=hue, palette=palette)

    if kind == "quantile":
        f = qqplot
    elif kind == "probability":
        f = ppplot
    else:
        msg = "kind must be either 'quantile' or 'probability'"
        raise ValueError(msg)

    grid.map(qqplot, **kws)

    # Add a legend
    if hue is not None:
        grid.add_legend()

    return grid
