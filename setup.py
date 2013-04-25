"""
CloudApp Example Site
~~~~~~~~~~~~~~~~~~~~~

Copyright 2013 Ryan Olson

This file is part of CloudApp-Example.

CloudApp is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

CloudApp is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with CloudApp.  If not, see <http://www.gnu.org/licenses/>.

"""
from setuptools import setup, find_packages

setup(
    name='Example',
    version='0.1dev',
    author='Quantum Coding',
    author_email='quantumcoding@gmail.com',
    packages=find_packages(exclude=["dependencies"]),
    zip_safe=False,
    platforms='any',
    install_requires=[
        'CloudApp',
        'celery'
    ],
    dependency_links = [
    ]
)
