#!/usr/bin/env python
# ----------------------------------------------------------------------- #
# Copyright 2008-2010, Gregor von Laszewski                               #
# Copyright 2010-2013, cloudmesh_data.org                                      #
#                                                                         #
# Licensed under the Apache License, Version 2.0 (the "License"); you may #
# not use this file except in compliance with the License. You may obtain #
# a copy of the License at                                                #
#                                                                         #
# http://www.apache.org/licenses/LICENSE-2.0                              #
#                                                                         #
# Unless required by applicable law or agreed to in writing, software     #
# distributed under the License is distributed on an "AS IS" BASIS,       #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.#
# See the License for the specific language governing permissions and     #
# limitations under the License.                                          #
# ------------------------------------------------------------------------#
from __future__ import print_function

import os
import platform
import sys

from setuptools import setup, find_packages

__version__ = '0.1.0'  # surpress the version error
# don't use import to get the version as that causes a circular dependency
#exec(open('cloudmesh_data/__init__.py').read().strip())

#
# TODO: update to the newest versions
#
# if sys.version_info > (3, 7, 0):
#    print(70 * "#")
#    print("WARNING: upgrade to a python greater than 3.7.0 "
#          "other version are not supported. Your version is {}. failed.".format(sys.version_info))
#    print(70 * "#")

command = None
this_platform = platform.system().lower()
if this_platform in ['darwin']:
    command = "easy_install readline"
elif this_platform in ['windows']:
    command = "pip install pyreadline"

if command is not None:
    print("Install readline")
    os.system(command)

requirements = map(str.strip, open('requirements.txt'))


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


home = os.path.expanduser("~")

# data_files= [
#    (os.path.join(home, '.cloudmesh_data'),
#    [os.path.join(d, f) for f in files]) for d, folders, files in os.walk(
#                os.path.join('cloudmesh_cm4', 'etc'))]
#
# print ("DDDD", data_files)

# package_data={
#   'cloudmesh_cm4.etc': ['*.yaml', '*.py'],
# },


setup(
    version=__version__,
    name="cloudmesh_data",
    description="cloudmesh_data - A heterogeneous multi cloud command "
                "client and shell",
    long_description=read('README.md'),
    license="Apache License, Version 2.0",
    author="Gregor von Laszewski, cloudmesh_data.org",
    author_email="laszewski@gmail.com",
    url="https://github.com/cloudmesh_data-community/cm",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering",
        "Topic :: System :: Clustering",
        "Topic :: System :: Distributed Computing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Console"
    ],
    keywords="cloud cmd commandshell plugins",
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    # data_files= data_files,
    # package_data={
    #     'cloudmesh_data.etc': ['*.yaml', '*.py'],
    # },

    entry_points={
        'console_scripts': [
            'cmdata = cloudmesh_data.data.command:main',
        ],
    },
    # tests_require=['tox'],
    # dependency_links = []
)
