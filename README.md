# mong

A Python port of [moby](https://github.com/moby/moby) name generator.

## Installation

```
$ pip install https://github.com/toshihikoyanase/mong.git
```

## Usage

```python
>>> import mong
>>> ng = mong.NameGenerator()
>>> ng.get_random_name()
'goofy_robinson'
>>> ng.get_random_name()
'stoic_feynman'
```

## References

- [Moby Project](https://mobyproject.org/)
- [moby/moby@GitHub](https://github.com/moby/moby)
