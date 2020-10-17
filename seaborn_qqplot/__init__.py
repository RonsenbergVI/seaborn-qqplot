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

import matplotlib.patches as patches
from matplotlib.pyplot import legend
from pandas import DataFrame, Series
from scipy.stats import rv_continuous, t
from seaborn import PairGrid, color_palette, utils

from seaborn_qqplot.plots import (
    ProbabilityPlot,
    QQPlot,
    PPPlot,
    QuantilePlot
)
from seaborn_qqplot.validation import (
    _validate_interpolation,
    _validate_kind,
    _validate_data,
    _validate_x_and_y
)

from seaborn_qqplot.version import version

__version__ = version


def pplot(data, 
        x=None, 
        y=None, 
        hue=None, 
        hue_order=None, 
        palette=None, 
        kind="q",
        height=2.5, 
        aspect=1, 
        scale='linear',
        interpolation='linear',
        dropna=True,
        plot_kws={},
        display_kws={}):
    """Draw a probability plot of one variable against a probability distribution or
    two variables.

    Parameters
    ----------
    data : DataFrame
        Tidy (long-form) dataframe where each column is a variable and
        each row is an observation.
    x : string, optional
        name of column in ``data``.
    y : string or `scipy.rv_continuous` instance, optional
        name of column in ``data`` or a probability distribution
    hue : string (variable name), optional
        Variable in ``data`` to map plot aspects to different colors.
    hue_order : list of strings
        Order for the levels of the hue variable in the palette
    palette : dict or seaborn color palette
        Set of colors for mapping the ``hue`` variable. If a dict, keys
        should be values  in the ``hue`` variable.
    kind : { "q" | "p" | "pp" | "qq" }, optional
        Kind of plot to draw.
    height : numeric, optional
        Size of the figure (it will be square).
    aspect : numeric, optional
        Ratio of joint axes height to marginal axes height.
    dropna : bool, optional
        If True, remove observations that are missing from ``x`` and ``y``.
    {dispay, plot}_kws : dicts, optional
        Additional keyword arguments for the plot components.
    kwargs : key, value pairings
        Additional keyword arguments are passed to the function used to
        draw the plot on the joint Axes.

    Returns
    -------
    grid : :class:`PairGrid`
        :class:`PairGrid` object with the plot on it.
    """

    validated_data = _validate_data(data, dropna)
    validated_x, validated_y = _validate_x_and_y(x,y)
    x_vars = [validated_x]

    if isinstance(validated_y, rv_continuous):
        discrete_y = validated_y(
            *validated_y.fit(validated_data[validated_x])
            ).rvs(
                len(validated_data[validated_x]
                )
            )
        name = "{}_dist".format(validated_y.name)
        validated_data[name] = Series(discrete_y, index=validated_data.index)
        y_vars=[name]
    else:
        y_vars = [validated_y]

    if display_kws is None:
        display_kws = {}

    kws = {"display_kws":display_kws, "plot_kws":plot_kws, 'interpolation': interpolation}

    grid = PairGrid(validated_data, x_vars=x_vars, y_vars=y_vars, height=height, aspect=aspect, hue=hue, palette=palette)

    kind = _validate_kind(kind)

    if kind == "qq":
        plot_map = QQPlot(**kws)
    elif kind == "pp":
        plot_map = PPPlot(**kws)
    elif kind == "p":
        plot_map = ProbabilityPlot(**kws)
    elif kind == "q":
        plot_map = QuantilePlot(**kws)

    grid.map(plot_map)

    if hue:
        labels = data[hue].unique()[::-1]
        n_colors = len(labels)
    
        # 'seabornic' handling of palettes
        current_palette = utils.get_color_cycle()
        if n_colors > len(current_palette):
            colors = color_palette("husl", n_colors)
        else:
            colors = color_palette(n_colors=n_colors)
        colors = colors.as_hex()[:len(labels)]
        handles = [patches.Patch(color=color, label=label) for color, label in zip(colors,labels)]
        legend(handles=handles)

    return grid
