from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()


setup(
    name='do_something',
    version='0.1.0',
    description='Python Mock Learning & Project Structuring Learning',
    long_description=readme,
    author='Quang Nguyen',
    author_email='nguyenvan.kwang193@gmail.com',
    packages=find_packages(exclude=('tests', 'docs'))
)

