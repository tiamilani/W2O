# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2022 Mattia Milani <mattia.milani10@gmail.com>

from setuptools import setup, find_packages

setup(
    name='W2O',
    version='0.0.1',
    description='Written 2 oral framework for exams',
    author='Mattia Milani',
    author_email='mattia.milani10@gmail.com',
    packages=find_packages(exclude=['W2O.tests*', 'ez_setup']),
    install_requires=[
        'PyYAML',
        'argparse',
        'numpy',
        'pandas',
        'xlrd',
        'openpyxl',
        'xlwt'
    ],
    setup_requires=['pytest-runner'],
    tests_requires=['pytest', 'pytest-cov'],
    package_data={'W2O': ['Conf/basic.yaml']},
    entry_points={
        'console_scripts': ['w2o=W2O.main:main']
    }
)
