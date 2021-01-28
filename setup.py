# Copyright © 2020  Hethsron Jedaël BOUEYA

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

from setuptools import setup, find_packages

"""
    @file       setup.py
    @details    Required file which exists in root of project directory
                to build and distribute package
    @author     BOUEYA Hethsron Jedaël <hethsron-jedael.boueya@uha.fr>
                BENOMAR Yassine <yassine.benomar@uha.fr>
    
    @version    0.0.1
    @date       October 23th, 2020
    @copyright  GPLv3+ : GNU GPL version 3 or later
                Licencied Material - Property of Stimul’Activ®
                © 2020 ENSISA (UHA) - All rights reserved.
"""

def readme():
    """!
        @fn     readme
        @brief  Returns detailed description of the package
    """
    with open('README.md') as f:
        return f.read()

def requirements():
    """!
        @fn     requirements
        @brief  Returns dependencies a project minimally needs to run
    """
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name = 'deepmwoo',
    version = '0.0.1',
    description = 'Facial Recognition Algorithm Using LBPH Algorithm',
    url = 'https://github.com/Hethsron/lbph',
    author = 'Hethsron Jedaël BOUEYA',
    author_email = 'hethsron-jedael.boueya@uha.fr',
    long_description = readme(),
    license = 'GPL-3.0',
    classifiers = [
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Deep Learning',
        'License :: GPL-3.0',
        'Programming language :: Python :: 3.8'
    ],
    keywords = [
        'Face detection',
        'Face Tracking',
        'Face recognition'
    ],
    project_urls = {
        'Documentation' : '',
        'Funding' : '',
        'Say Thanks !' : '',
        'Source' : 'https://github.com/Hethsron/lbph',
        'Tracker' : 'https://github.com/Hethsron/lbph/issues'
    },
    packages = find_packages(include = [
        'lbph'
    ]),
    plateformes = 'ALL',
    python_requires = '>=3.7',
    install_requires = requirements(),
    zip_safe = False
)