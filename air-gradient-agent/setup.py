from setuptools import setup

setup(
   name='air_gradient_agent',
   version='1.0',
   description='Save air gradient sensor information to influxdb',
   author='Andy Baumgartner',
   author_email='andybaumgar@gmail.com',
   packages=['air_gradient_agent'],  #same as name
   install_requires=[], #external packages as dependencies
)