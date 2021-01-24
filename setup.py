#!/usr/bin/env python3

import os
import datetime
from setuptools import setup

# get key package details from githubactioncontexthelper/__version__.py
about = {}  # type: ignore
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'githubactioncontexthelper', '__version__.py')) as f:
    exec(f.read(), about)

# load the README file and use it as the long_description for PyPI
with open('README.md', 'r') as f:
    readme = f.read()

# package configuration - for reference see:
# https://setuptools.readthedocs.io/en/latest/setuptools.html#id9
#     version=f'{about["__version__"]}.{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}',

setup(
    name=about['__title__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    version=f'{about["__version__"]}',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=['githubactioncontexthelper'],
    include_package_data=True,
    python_requires=">=3.8.*",
    install_requires=['setuptools'],
    license=about['__license__'],
    zip_safe=False,
    # entry_points={
    #     'console_scripts': ['py-package-template=githubactioncontexthelper.contexthandler:main'],
    # },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='package development template'
)
