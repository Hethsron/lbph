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
    @file       train.py
    @brief      Basic Processing Algorithm to perform model training
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

import cv2, os
import numpy as np

class training(object):
    """!
        @class      training
        @brief      Define useful static methods which implements various
                    techniques such as :
                        - Training process
    """

    @staticmethod
    def build_labels(datasets_path = None):
        """!
            @fn     __build_labels__
            @brief  Get images and label data

             @param[in]      datasets_path        Relative of Absolute path to the datasets
             @return         images, labels, dict_labels
        """

        # Define face samples
        images = []

        # Define face labels
        labels = []

        # Define labels dictionnary
        dict_labels = {}

        # Get peoples
        people = [person for person in os.listdir('datasets')]

        for i, person in enumerate(people):
            # Append person to dictionnay
            dict_labels[i] = person

            for image in os.listdir('datasets/' + person):
                images.append(cv2.imread('datasets/' + person + '/' + image, 0))
                labels.append(i)
        
        # Creates numpy array of collected labels
        labels = np.array(labels)

        return images, labels, dict_labels
 
    @staticmethod
    def make(datasets_path = None):
        """!
            @fn     make
            @brief  Perform training process

             @param[in]      datasets_path        Relative of Absolute path to the datasets
        """

        # Create LBPH face recognizer algorithm
        recognizer = cv2.face.LBPHFaceRecognizer_create()

        # Load Haar classifier
        detector = cv2.CascadeClassifier("res/haarcascade_frontalface_default.xml");

       # Displaying message
        print("[+] Initiating The Training Process ...")
        print("[+] It Will Take A Few Seconds. Wait  ...")

        # Get images and labels data
        faces, ids, _ = training.build_labels(datasets_path = datasets_path)
        recognizer.train(faces, np.array(ids))

        # Save the model into models/mwoo.yml
        recognizer.write('models/mwoo.yml')

        # Print the numer of faces trained and end program
        print("[+] There Are {0} Faces Trained".format(len(np.unique(ids))))
        print("[+] End Of The Training Process")
