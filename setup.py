from setuptools import setup


def load_readme() -> str:
    with open("README.md") as fin:
        return fin.read()


setup(
    name="mong",
    version="0.0.3a",
    description="Moby Name Generator in Python",
    long_description=load_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/toshihikoyanase/mong",
    author="Toshihiko Yanase",
    author_email="toshihiko.yanase@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=["mong"],
    package_data={"mong": ["moby_dict.json"]},
)
