import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand
from datascience.version import __version__


if sys.version_info < (3, 6):
    raise ValueError('This package requires python >= 3.6')

with open('requirements.txt') as fid:
    install_requires = [l.strip() for l in fid.readlines() if l]

tests_requires = [
    'pytest',
    'coverage',
    'coveralls',
    'bokeh'
]

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ['--nbval-lax', '--cov=datascience', 'tests']

    def finalize_options(self):
        TestCommand.finalize_options(self)

    def pytest_collectstart(collector):
        collector.skip_compare += 'text/html'

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name = 'datascience',
    packages = ['datascience'],
    python_requires='>=3.6',
    version = __version__,
    install_requires = install_requires,
    tests_require = tests_requires,
    cmdclass = {'test': PyTest},
    description = 'A Jupyter notebook Python library for introductory data science',
    long_description = 'A Jupyter notebook Python library for introductory data science',
    author = 'John DeNero, David Culler, Alvin Wan, Sam Lau',
    author_email = 'ds8-instructors@berkeley.edu',
    url = 'https://github.com/data-8/datascience',
    download_url = 'https://github.com/data-8/datascience/archive/%s.zip' % version,
    keywords = ['data', 'tools', 'berkeley'],
    classifiers = [],
    package_data={"datascience": ["geodata/*.csv"]}
)
