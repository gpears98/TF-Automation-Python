from setuptools import setup, find_packages


with open('../README.rst') as f:
    readme = f.read()

with open('../LICENSE') as f:
    pylicense = f.read()

setup(
    name='AgentDetails',
    version='0.1.0',
    description='This package contains static modules to acquire'
                'cloud agent environment variables.',
    long_description=readme,
    author='Garrett Pearson',
    author_email='garrett.pearson@united.com',
    license=pylicense,
    packages=find_packages(exclude=('tests', 'docs'))
)
