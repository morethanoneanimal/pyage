# coding=utf-8
from paver.easy import *
from paver.setuputils import setup
from setuptools import find_packages

setup(
    name="pyage",
    description="Python Agent-based evolution",
    packages=find_packages(),
    version="0.9.7",
    author="Maciej Kaziród",
    author_email="kmaciej@student.agh.edu.pl",
    requires=['Pyro4(==4.17)']
)


@task
@needs('generate_setup', 'minilib', 'setuptools.command.sdist')
def sdist():
    """Overrides sdist to make sure that our setup.py is generated."""
    pass


@task
@needs("setuptools.command.bdist_egg")
def egg():
    pass
