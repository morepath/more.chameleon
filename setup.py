import os, io
from setuptools import setup, find_packages

long_description = (
    io.open('README.rst', encoding='utf-8').read()
    + '\n' +
    io.open('CHANGES.txt', encoding='utf-8').read())

setup(name='more.chameleon',
      version='0.1',
      description="Chameleon template integration for Morepath",
      long_description=long_description,
      author="Martijn Faassen",
      author_email="faassen@startifact.com",
      keywords='morepath chameleon',
      license="BSD",
      url="http://pypi.python.org/pypi/more.chameleon",
      namespace_packages=['more'],
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'morepath >= 0.10',
        'chameleon >= 2.20'
        ],
      extras_require = dict(
        test=['pytest >= 2.6.0',
              'pytest-cov',
              'WebTest'],
        ),
      )
