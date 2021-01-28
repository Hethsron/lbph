#!/usr/bin/env python3

# Copyright © 2020  Hethsron Jedaël BOUEYA and Yassine BENOMAR

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

"""!
    @file       access.py
    @brief      Basic Access Manager For Facial Recognition Algorithm Using Deep Learning
    @details    
    
    @author     BOUEYA Hethsron Jedaël <hethsron-jedael.boueya@uha.fr>
                BENOMAR Yassine <yassine.benomar@uha.fr>
    
    @version    0.0.1
    @date       October 23th, 2020
    
    @note       For this program, we recommand to use the existing virtual
                environment that allows you to avoid installing Python
                packages globally which could break system tools or other projects 
    
    @pre        Before you can start installing or using packages in the
                existing virtual environment, you'll need to activate it.
                Activating this virtual environment will put the virtual
                environment-specifi python and pip executables into your
                shell's PATH.
                    -   On macOS and Linux, run :
                            source env/bin/activate
                    -   On Windows, run :
                            .\env\Scripts\activate
    @post       If you want to switch projects or otherwise leave this virtual
                environment, simply run :
                            deactivate
    @bug        No known bug to date
    @warning    Misuse could cause program crash
    @attention
    @remark
    @copyright  GPLv3+ : GNU GPL version 3 or later
                Licencied Material - Property of Stimul’Activ®
                © 2020 ENSISA (UHA) - All rights reserved.
"""

import filetype, os, re

class argv(object):
    """!
        @class      argv
        @brief      Define useful static methods to control given argument
    """

    @staticmethod
    def is_device(given_argv = None):
        """!
            @fn     is_device
            @brief  Returns True if given argument is a valid device, False otherwise
            @param[in]      given_argv      Given argument
            @return         True if given_argv is a valid device, False otherwise
        """
        # Check if pattern matches with given argument
        if re.compile('^(VID[0-2])|(vid[0-2])$').match(given_argv):
            # Return True statement
            return True
        # Return False statement
        return False

    @staticmethod
    def is_image(given_argv = None):
        """!
            @fn     is_image
            @brief  Returns True if given argument is a valid readable image, False otherwise
            @param[in]      given_argv      Given argument
            @return         True if given_argv is a valid readable image, False otherwise
        """
        # Check if given argument is an existing and readable file image
        if os.path.isfile(given_argv) and os.access(given_argv, os.R_OK) and filetype.is_image(given_argv):
            # Return True statement
            return True
        # Return False statement
        return False

    @staticmethod
    def is_video(given_argv = None):
        """!
            @fn     is_video
            @brief  Returns True if given argument is a valid readable video, False otherwise
            @param[in]      given_argv      Given argument
            @return         True if given_argv is a valid readable video, False otherwise
        """
        # Check if given argument is an existing and readable file video
        if os.path.isfile(given_argv) and os.access(given_argv, os.R_OK) and filetype.is_video(given_argv):
            # Return True statement
            return True
        # Return False statement
        return False

    @staticmethod
    def is_remote_device(given_argv = None):
        """!
            @fn     is_remote_device
            @brief  Returns True if given argument is a valid remote device, False otherwise
            @param[in]      given_argv      Given argument
            @return         True if given_argv is a valid remote device, False otherwise
        """
        pass