from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='mrsmith-rebelkeithy',
    version='0.0.5',
    author='Mitchell Manning',
    author_email='mitchellmanning@gmail.com',
    description='A library to generate random names',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/RebelKeithy/mrsmith',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={
        "": ["*.data"],
    }
)