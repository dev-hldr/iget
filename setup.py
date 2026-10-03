from setuptools import setup

setup(
    name = 'iget',
    version= '0.1',
    packages= ['iget'],
    entry_points = {
        'console_scripts' : ['iget = iget.cli:main']
    }
)