from os.path import join, dirname
from setuptools import setup, find_packages

import config_parser

setup(
    name='config_parser',
    version=config_parser.__version__,
    packages=find_packages(),
)
