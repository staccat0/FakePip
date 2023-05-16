from setuptools import setup
from setuptools.command.install import install
import base64
import os



setup(name='FakePip', version='0.0.1', description='This will exploit a sudoer able to /usr/bin/pip install *',
      url='https://github.com/staccat0/fakepip', author='zc00l', author_email='andre.marques@esecurity.com.br',
      license='MIT', zip_safe=False)
