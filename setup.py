#!/usr/bin/python
#-*-coding:utf-8-*-
from setuptools import setup,find_packages
setup(name='AutoDownLoadNorvel',
      version='1.0',
      packages=["norvel"],
      include_package_file=True,
      install_requires=['requests','bs4','concurrent',],
      entry_points={'console_scripts':['down-norvel=norvel:main']},)