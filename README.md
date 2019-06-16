# seaborn-qqplot

seaborn extension that adds qqplots and ppplots.

[![Documentation Status](https://readthedocs.org/projects/seaborn-qqplot/badge/?version=latest)](https://seaborn-qqplot.readthedocs.io/en/latest/?badge=latest)



## Documentation

The documentation can be found [here](http://seaborn-qqplot.readthedocs.io/en/latest/).

## Contributing

Contribution will be welcomed once a first stable release is ready.


## Quickstart

The extension wants to be as similar as seaborn as possible.

```python
import seaborn_qqplot as sqp
```

The example provided with the package is the Iris dataset:

```python
import seaborn as sns

iris_data = sns.load_dataset('iris')
```

### 1. Simple qq-plot

A qq-plot can be easily displayed using the `sqp.qqplot` method:






## Future Development

I hope to add very soon probability-probability plots (pp-plots).

## Requirements

These requirements reflect the testing environment.  It is possible
that seaborn-qqplot will work with older versions.

* Python (3+)
* NumPy (1.16+)
* SciPy (1.2+)
* Pandas (0.23+)

## Support or Contact

Having trouble with seaborn-qqplot? Check out the [documentation](http://seaborn-qqplot.readthedocs.io/en/latest/).

Issues can be flagged [here](https://github.com/ronsenbergVI/seaborn-qqplot/issues).
