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

from sqp import qqplot, ppplot

def qqnorm(x, data = None, fit_reg = False,  palette = None, ax = None):
    pass

def qq(x, y = None, dist = None, data = None, hue = None, height = None, aspect = None, fit_reg = False, palette = None, ax = None):
    """
    """
    g = FacetGrid(data, height = height, aspect = aspect)
    g.map(qqplot, x, y, dist = dist, col = hue, color = mycolor, fit_reg = fit_reg)

def pp(x, y = None, dist = None, data = None, hue = None, height = None, aspect = None, fit_reg = False, palette = None, ax = None):
    """
    """
    if not palette is None:
        mycolor = (palette[2][0],palette[2][1],palette[2][2])
    else:
        mycolor = None
    g = FacetGrid(data, height = height, aspect = aspect)
    g.map(ppplot, x, y, dist = dist, col = hue, color = mycolor, fit_reg = fit_reg)
