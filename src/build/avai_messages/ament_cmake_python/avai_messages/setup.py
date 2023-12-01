from setuptools import find_packages
from setuptools import setup

setup(
    name='avai_messages',
    version='0.0.1',
    packages=find_packages(
        include=('avai_messages', 'avai_messages.*')),
)
