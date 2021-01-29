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
    @file       capture.py
    @brief      Basic Processing Algorithm to capture faces from camera
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

class shooting(object):
    """!
        @class      shooting
        @brief      Define useful static methods which implements various
                    techniques such as :
                        - Face extraction for training process
    """

    @staticmethod
    def __take__(video_source = None, path = None, detector = None, lower = int(), upper = int()):
        """!
            @fn             __take__
            @brief          Take shooting photo for training process

            @param[in]      video_source        Source video file to capture frame by frame
            @param[in]      path                Directory of images
            @param[in]      detector            Haar Cascade classifier
            @param[in]      lower               Lower bound interval of face count
            @param[in]      upper               Upper bound interval of face count
        """

        # Create a VideoCapture object
        cap = cv2.VideoCapture(video_source)

        # Define video resolution (width * height)
        cap.set(3, 640)
        cap.set(4, 480)

        # Initialize individual sampling face count
        counter = lower

        # Start detect your face and take 50 pictures
        while(True):
            # Read image
            ret, img = cap.read()

            # Convert the image to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)     
                counter += 1

                # Save the captured image into the datasets folder
                cv2.imwrite(path + '/' + str(counter) + '.jpg', gray[y:y + h, x:x + w])
                cv2.imshow('<-> MWOO <->', img)

            # Check user interruptions
            # Press 'ESC' for exiting video
            k = cv2.waitKey(100) & 0xff
            if k == 27:
                break
            elif counter >= upper:
                # Take faces sample and stop video
                break
        
        # Do a bit of cleanup
        cap.release()
        cv2.destroyAllWindows()

    @staticmethod
    def make(video_source = None):
        """!
            @fn             make
            @brief          Capture live stream and make shooting photo for training process
            @param[in]      video_source        Source video file to capture frame by frame  
        """

        # Take the name of new person
        name = input('[+] What Is The Name Of New Person To Add ?  ').lower()

        # Specify the new directory relative path
        path = 'datasets/' + name

        # Check if the data for the given person already exist
        if not os.path.exists(path):
             # Displaying message
            print('[+] Initiating The Shooting Process ...')
            print('[+] Look At The Camera ...')
            input('[+] We Are Going To Take 50 Pictures. Press [ENTER] When You Are Ready ...')

            # Create new folder
            os.mkdir(path)

            # Take front pictures
            print('[+] Take front pictures ...')
            shooting.__take__(video_source = video_source, 
                                path = path, 
                                detector = cv2.CascadeClassifier('res/haarcascade_frontalface_default.xml'),
                                lower = 0,
                                upper = 25)

            # Take profile pictures
            print('[+] Take profile pictures ...')
            shooting.__take__(video_source = video_source, 
                                path = path, 
                                detector = cv2.CascadeClassifier('res/haarcascade_profileface.xml'),
                                lower = 25,
                                upper = 50)

            # Do a bit of cleanup
            print('[+] End Of The Capturing Process')
        else:
            print('[-] This Person Already Exists In The Datasets')
            pass