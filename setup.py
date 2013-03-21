#!/usr/bin/env python
#
# Copyright (c) SAS Institute Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from distutils.core import setup, Extension

setup(
    name='python-keyutils',
    version='0.1',
    description='keyutils bindings for Python',
    author='Mihai Ibanescu',
    author_email='misa@rpath.com',
    url='http://www.rpath.com',
    license='Apache 2.0',
    packages=['keyutils'],
    ext_modules=[
        Extension(
            'keyutils._keyutils', ['keyutils/_keyutils.c'], libraries=['keyutils'],
        )
    ],
)
