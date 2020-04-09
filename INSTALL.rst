Installing trendpy
------------------

Installation with pip (recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The library is available on pypi and to install the last available version, run this command:

.. code-block:: bash

    $ pip install seaborn-qqplot

To test the installation:

    >>> import seaborn_qqplot as sqp
    >>> sqp.__version__

this should display the version installed on your system.

Installation from GitHub
^^^^^^^^^^^^^^^^^^^^^^^^

seaborn-qqplot releases are also available on github (https://github.com/ronsenbergVI/seaborn-qqplot).
You first need to clone (or fork if you want to modify it) and

.. code-block:: bash

		$ git clone https://github.com/ronsenbergVI/seaborn-qqplot.git
		$ cd seaborn-qqplot
		$ python setup.py build
		$ python setup.py install
