# mong

A Python port of [moby](https://github.com/moby/moby) name generator.
The original code in [moby](https://github.com/moby/moby) can be found [here](https://github.com/moby/moby/blob/master/pkg/namesgenerator/names-generator.go).

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
