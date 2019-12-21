from distutils.core import setup


setup(name='mong',
      version='0.0.1',
      description='Moby Name Generator in Python',
      author='Toshihiko Yanase',
      author_email='toshihiko.yanase@gmail.com',
      packages=['mong'],
      package_data={'mong': ['moby_dict.json']},
     )
