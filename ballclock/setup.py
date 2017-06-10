"""
Author: Jeremy Cornett
Date: 06/10/2017
Purpose: This file is used by SetupTools for creating the package itself.
Assumptions: Python and Pip are installed.
"""

from setuptools import setup


def readme():
    """Display the contents of the readme file."""
    with open('README.md') as f:
        return f.read()


setup(name='theclock',
      version='1.0.0',
      description='A coding exercise focused on the classic construct of a ball clock machine.',
      url='https://github.com/jeremycornett/BallClock',          # The url to download this package from.
      author='Jeremy Cornett',
      author_email='cornett.jeremy@gmail.com',
      packages=['theclock'],
      install_requires=[],                            # Required pip packages in order to run this package.
      setup_requires=['pytest-runner'],
      tests_require=['pytest', "pytest-cov"],
      zip_safe=False,
      include_package_data=True)
