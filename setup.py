# This file is autogenerated by medikit code generator.
# All changes will be overwritten.

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Py3 compatibility hacks, borrowed from IPython.
try:
    execfile
except NameError:

    def execfile(fname, globs, locs=None):
        locs = locs or globs
        exec(compile(open(fname).read(), fname, "exec"), globs, locs)


# Get the long description from the README file
try:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''

# Get the classifiers from the classifiers file
tolines = lambda c: list(filter(None, map(lambda s: s.strip(), c.split('\n'))))
try:
    with open(path.join(here, 'classifiers.txt'), encoding='utf-8') as f:
        classifiers = tolines(f.read())
except:
    classifiers = []

version_ns = {}
try:
    execfile(path.join(here, 'bonobo/_version.py'), version_ns)
except EnvironmentError:
    version = 'dev'
else:
    version = version_ns.get('__version__', 'dev')

setup(
    author='Romain Dorgueil',
    author_email='romain@dorgueil.net',
    description=('Bonobo, a simple, modern and atomic extract-transform-load toolkit for '
                 'python 3.5+.'),
    license='Apache License, Version 2.0',
    name='bonobo',
    version=version,
    long_description=long_description,
    classifiers=classifiers,
    packages=find_packages(exclude=['ez_setup', 'example', 'test']),
    include_package_data=True,
    install_requires=[
        'colorama (>= 0.3)', 'fs (>= 2.0, < 2.1)', 'jinja2 (>= 2.9, < 2.10)', 'mondrian', 'packaging (>= 16, < 17)',
        'psutil (>= 5.4, < 6.0)', 'requests (>= 2.0, < 3.0)', 'stevedore (>= 1.27, < 1.28)', 'whistle (== 1.0a3)'
    ],
    extras_require={
        'dev': [
            'coverage (>= 4.4, < 5.0)', 'pytest (>= 3.1, < 4.0)', 'pytest-cov (>= 2.5, < 3.0)',
            'pytest-sugar (>= 0.8, < 0.9)', 'pytest-timeout (>= 1, < 2)', 'sphinx (>= 1.6, < 2.0)', 'yapf'
        ],
        'docker': ['bonobo-docker (>= 0.5.0)'],
        'jupyter': ['ipywidgets (>= 6.0.0, < 7)', 'jupyter (>= 1.0, < 1.1)'],
        'sqlalchemy': ['bonobo-sqlalchemy (>= 0.5.1)']
    },
    entry_points={
        'bonobo.commands': [
            'convert = bonobo.commands.convert:ConvertCommand', 'init = bonobo.commands.init:InitCommand',
            'inspect = bonobo.commands.inspect:InspectCommand', 'run = bonobo.commands.run:RunCommand',
            'version = bonobo.commands.version:VersionCommand', 'download = bonobo.commands.download:DownloadCommand'
        ],
        'console_scripts': ['bonobo = bonobo.commands:entrypoint']
    },
    url='https://www.bonobo-project.org/',
    download_url='https://github.com/python-bonobo/bonobo/tarball/{version}'.format(version=version),
)
