
from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    README = f.read()

setup(name='olibox-control',


      version='0.1dev1',
      description='OLI Box Code to subscribe channels and send commands to control the olibox devices',
      long_description=README,
      long_description_content_type="text/markdown",

      author='Muhammad Yahya & Felix Forster @ OLI Systems 2020',
      url='https://github.com/olisystems/olibox-control.git',
      packages=['olibox_control.control_pkg',
                'olibox_control'],
      install_requires=['click', 'toml', 'paho-mqtt', ],

      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: Utilities",
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: Operating System :: POSIX :: Linux", ],

      entry_points={
          'console_scripts': [
              'olibox-control = olibox_control.olibox_control:main'
          ]
      },

      )
