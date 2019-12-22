from distutils.core import setup


def load_readme() -> str:
    with open('README.md') as fin:
        return fin.read()


setup(name='mong',
      version='0.0.1',
      description='Moby Name Generator in Python',
      long_description=load_readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/toshihikoyanase/mong',
      author='Toshihiko Yanase',
      author_email='toshihiko.yanase@gmail.com',
      packages=['mong'],
      package_data={'mong': ['moby_dict.json']})
