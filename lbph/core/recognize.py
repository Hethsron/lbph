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
    @file       recognize.py
    @brief      Basic Processing Algorithm for recognition
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

import cv2, os, time
import numpy as np
from lbph.core.train import training

class recognition(object):
    """!
        @class      recognition
        @brief      Define useful static methods which implements various
                    techniques such as :
                        - Face recognition
    """

    @staticmethod
    def fromStream(video_source = None):
        """!
            @fn             fromStream
            @brief          Perform face recognition process

            @param[in]      video_source        Source video file to capture frame by frame 
        """

        # Create LBPH face recognizer algorithm
        recognizer = cv2.face.LBPHFaceRecognizer_create()

        # Load pre-trained model
        recognizer.read('models/mwoo.yml')
        
        # Load front Haar Classifier
        front_detector = cv2.CascadeClassifier('res/haarcascade_frontalface_default.xml')

        # Load profile Haar Classifier
        profile_detector = cv2.CascadeClassifier('res/haarcascade_profileface.xml')

        prev_frame_time = 0
        new_frame_time = 0

        # key in names, start from the second place, leave first empty
        _, _, names = training.build_labels(datasets_path = 'datasets')

        # Create a VideoCapture object
        cap = cv2.VideoCapture(video_source)

        # Define video resolution (width * height)
        cap.set(3, 640)
        cap.set(4, 480)

        # Define min window size to be recognized as a face
        minW = 0.1 * cap.get(3)
        minH = 0.1 * cap.get(4)

        # Displaying message
        print("[+] Initiating The Recognition Process ...")
        print("[+] Look At The Camera And Wait ...")

        while True:
            # Read image
            ret, img = cap.read()

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            new_frame_time  = time.time()
            fps = 1 / (new_frame_time - prev_frame_time)
            prev_frame_time = new_frame_time
            fps = int(fps) 
            fps = str(fps)
            cv2.putText(img, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)

            # Detects objects of different sizes in the input image and return as a list of rectangles
            faces = front_detector.detectMultiScale(
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH))
            )

            # Check if list of rectangles is empty
            if not len(faces):
                faces = profile_detector.detectMultiScale(
                    gray,
                    scaleFactor = 1.2,
                    minNeighbors = 5,
                    minSize = (int(minW), int(minH))
                )

            for (x, y, w, h) in faces:
                # Draw rectangle around detected face
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # What you get as "confidence", is actually the opposite - the distance to the closest item in the database.
                id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

                # Check if confidence is less then 100 ==> "0" is perfect match
                if (confidence < 100):
                    id = names[id]
                    confidence = "  {0}%".format(round(100 - confidence))
                else:
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))

                # Put name and confidence
                cv2.putText(img, str(id), (x + 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv2.putText(img, str(confidence), (x + 5, y + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 1)

            cv2.imshow('<-> MWOO <->', img)

            # Check user interruptions
            # Press 'ESC' for exiting video
            k = cv2.waitKey(10) & 0xff
            if k == 27:
                break

        # Do a bit of cleanup
        print("[+] End Of Recognition Process")
        cap.release()
        cv2.destroyAllWindows()

    @staticmethod
    def fromImage(image_source = None):
        """!
            @fn             fromImage
            @brief          Perform face recognition process

            @param[in]      image_source        Source image file to capture frame by frame 
        """

        # Create LBPH face recognizer algorithm
        recognizer = cv2.face.LBPHFaceRecognizer_create()

        # Load pre-trained model
        recognizer.read('models/mwoo.yml')
        
        # Load front Haar classifier
        front_detector = cv2.CascadeClassifier('res/haarcascade_frontalface_default.xml')

        # Load profile Haar Classifier
        profile_detector = cv2.CascadeClassifier('res/haarcascade_profileface.xml')

        prev_frame_time = 0
        new_frame_time = 0

        # key in names, start from the second place, leave first empty
        _, _, names = training.build_labels(datasets_path = 'datasets')

        # Read an image with its default color
        img = cv2.imread(image_source)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        new_frame_time  = time.time()
        fps = 1 / (new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time
        fps = int(fps) 
        fps = str(fps) 
        cv2.putText(img, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)

        # Detects objects of different sizes in the input image and return as a list of rectangles
        faces = front_detector.detectMultiScale(
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH))
        )

        # Check if list of rectangles is empty
        if not len(faces):
            faces = profile_detector.detectMultiScale(
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH))
            )

        for (x, y, w, h) in faces:
            # Draw rectangle around detected face
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # What you get as "confidence", is actually the opposite - the distance to the closest item in the database.
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            # Check if confidence is less then 100 ==> "0" is perfect match
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

            # Put name and confidence
            cv2.putText(img, str(id), (x + 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 1)

        cv2.imshow('<-> MWOO <->', img)
        
        # Check user interruptions
        cv2.waitKey(0)

        # Do a bit of cleanup
        print("[+] End Of Recognition Process")
        cv2.destroyAllWindows()