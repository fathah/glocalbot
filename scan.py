import cv2
import numpy as np
from pandas import read_json
import pyzbar.pyzbar as pyzbar

def scanQr():
    jmId = ""
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            if "JM" in str(obj.data):
                jmId = str(obj.data)
                jmId = jmId.replace("b'","")
                jmId = jmId.replace("'","")
                jmId = jmId.split("@")[0]
            
                return jmId
    

def getStudentInfo(jamiaId):
    students = read_json("students.json")
    for student in students['data']:
        if student['jamiaId'] == jamiaId:
            return student
        else:
            pass