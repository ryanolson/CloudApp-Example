"""
CloudApp Example Site
~~~~~~~~~~~~~~~~~~~~~

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
