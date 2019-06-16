==============
seaborn-qqplot
==============

.. module:: seaborn-qqplot

**seaborn-qqplot** is a seaborn extension adding qqplots.


User's Guide
============

Requirements
------------

seaborn-qqplot is build on top of the following libraries:

* `Numpy` (http://www.numpy.org)
* `SciPy` (http://www.scipy.org)
* `Pandas` (http://pandas.pydata.org/)
* `matplotlib` (http://http://matplotlib.org/)


Issues
------

Should you encounter any issue with the library you can raise them here: https://github.com/ronsenbergVI/seaborn-qqplot/issues

.. include:: ../INSTALL.rst



Quickstart
==========

A simple qq-plot comparing the iris dataset petal length and sepal length distributions
can be done as follows:

  >>> import seaborn_qqplot as sqp
  >>> import seaborn as sns
  >>> iris = sns.load_dataset('iris')
  >>> qqplot(iris, x="petal_length", y="sepal_length")

.. _is_sweaty:
.. figure::  images/fig1.png
   :align:   center

   Simple qqplot


Seaborn-qqplot Changelog
=========================

We detail here the changes made to the library

.. include:: ../CHANGES


License
=======

seaborn-qqplot is licensed under the BSD 3-Clause License.
It means that the source code provided in the binaries can be used, modified,
or distributed freely for commercial or personal use with conditions only
requiring preservation of copyright and license notices.

The full license text can be found below (:ref:`seaborn-qqplot-license`).

Authors
-------

.. include:: ../AUTHORS

Contributing
------------

.. include:: ../CONTRIBUTING

License Definitions
-------------------

The following section contains the full license texts for seaborn-qqplot and the
documentation.

-   "AUTHORS" hereby refers to all the authors listed in the
    :ref:`authors` section.

-   The ":ref:`seaborn-qqplot-license`" applies to all the source code shipped as
    part of seaborn-qqplot (seaborn-qqplot itself as well as the examples and the unittests)
    as well as documentation.

:seaborn-qqplot-license

seaborn-qqplot License
----------------------

.. include:: ../LICENSE
