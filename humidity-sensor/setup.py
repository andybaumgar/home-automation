from setuptools import setup

setup(
   name='humidity_agent',
   version='1.0',
   description='Save temperature and humidity information',
   author='Andy Baumgartner',
   author_email='andybaumgar@gmail.com',
   packages=['humidity_agent'],  #same as name
   install_requires=[], #external packages as dependencies
)