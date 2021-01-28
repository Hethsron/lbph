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
    @file       main.py
    @brief      Facial Recognition Algorithm Using LBPH Algorithm
    @details    Declaration of starting point of this program
    
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
import os, sys, glob
from art import tprint
from lbph.core.capture import shooting
from lbph.core.train import training
from lbph.core.recognize import recognition
from lbph.core.access import argv
from getopt import getopt, GetoptError

class mwoo(object):
    """!
        @class      mwoo
        @brief      Define useful static methods to run `LBPH`.
    """

    @staticmethod
    def __version__():
        """!
            @fn     __version__
            @brief  Display information about `LBPH` release.
        """
        tprint('LBPH', font = 'bulbhead')
        print('Version 0.0.1')
        print('License GPLv3+ : GNU GPL version 3 or later')
        print('Licencied Material - Property of Stimul’Activ®')
        print('© 2020 ENSISA (UHA) - All rights reserved.')

    @staticmethod
    def __usage__():
        """!
            @fn     __usage__
            @brief  Display most of command line options that you can use
                    with `LBPH`.
        """
        if sys.platform in ('win32', 'win64'):
            pass
        else:
            os.system('clear')
            os.system('groff -Tascii -man lbph.man')

    @staticmethod
    def main():
        """!
            @fn     main
            @brief  Parse and interpret options.
        """
        try:
            opts, args = getopt(sys.argv[1:], 'chi:trv', [ 'capture', 'help', 'image=', 'train', 'recognize', 'version' ])
        except GetoptError as err:
            print(err)

            # Unsucessful termination occurs when parsing command-line options
            sys.exit(2)

        for o, a in opts:
            if o in ('-c', '--capture'):
                # Check if there is no argument
                if not args:
                    # Make a shooting of 30 pictures
                    shooting.make(video_source = 0)
                else:
                    # Built-in assert statement to find errors
                    assert False, 'The command does not run if the argument is provided'
            elif o in ('-h', '--help'):
                # Check if there is no argument
                if not args:
                    # Display usage of the application
                    mwoo.__usage__()
                else:
                # Built-in assert statement to find errors
                    assert False, 'The command does not run if the argument is provided'
            elif o in ('-i', '--image'):
                # Check if given argument is a valid readable image
                if argv.is_image(given_argv = a):
                    # Built-in tracking
                    recognition.fromImage(id = 1, image_source = a)
                else:
                    # Built-in assert statement to find errors
                    assert False, 'Invalid argument'
            elif o in ('-t', '--train'):
                # Check if there is no argument
                if not args:
                    training.make(datasets_path = 'datasets')
                else:
                    # Built-in assert statement to find errors
                    assert False, 'The command does not run if the argument is provided'
            elif o in ('-r', '--recognize'):
                # Check if given argument is a valid integer
                if not args:
                    recognition.fromStream(id = 1, video_source = 0)
                else:
                    # Built-in assert statement to find errors
                    assert False, 'The command does not run if the argument is provided'
            elif o in ('-v', '--version'):
                # Check if there is no argument
                if not args:
                    mwoo.__version__()
                else:
                    # Built-in assert statement to find errors
                    assert False, 'The command does not run if the argument is provided'
            else:
                # Built-in assert statement to find errors
                assert False, 'Unhandled option'

        # No problems occured (successful termination)
        sys.exit(0)

if __name__ == '__main__':
    mwoo.main()