from setuptools import setup

setup(
   name='example_install',
   version='1.0',
   description='example to show how setup installs',
   author='Trevor Sleight',
   author_email='twsleight@gmail.com',
   packages=['example_install'],  #same as name
   install_requires=['numpy~=1.19', 'pandas>=1.1'], #external packages as dependencies
   setup_requires=['pytest-runner'],
   tests_require=['pytest', 'test_square']
)