# mong

[![Python](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org)
[![pypi](https://img.shields.io/pypi/v/mong.svg)](https://pypi.python.org/pypi/mong)
![](https://github.com/toshihikoyanase/mong/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/toshihikoyanase/mong/branch/master/graph/badge.svg)](https://codecov.io/gh/toshihikoyanase/mong)

A Python port of [moby](https://github.com/moby/moby) name generator.
The original code in [moby](https://github.com/moby/moby) can be found [here](https://github.com/moby/moby/blob/master/pkg/namesgenerator/names-generator.go).

## Installation

```
# PyPI
$ pip install mong

# Development version
$ pip install git+https://github.com/toshihikoyanase/mong.git
```

## Usage

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/16iw3njq06R32-0dHiRn2efUvvZmYHeRL)

```python
>>> import mong
>>> mong.get_random_name()
'goofy_robinson'
>>> mong.get_random_name()
'stoic_feynman'
```

## References

- [Moby Project](https://mobyproject.org/)
- [moby/moby@GitHub](https://github.com/moby/moby)
