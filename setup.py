from setuptools import setup

setup(
    name='gcc_script',
    version='0.0.0',
    packages=['gcc_script'],
    entry_points = {
        'console_scripts': ['gcc_script=gcc_script.main:main'],
    }
)