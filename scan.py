import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

def scanQr():
    jmId = ""
    cap = cv2.VideoCapture(0)
    while True:
        print("Scanning")
        _, frame = cap.read()
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            if "JM" in str(obj.data):
                jmId = obj.data
                return jmId
    

            
