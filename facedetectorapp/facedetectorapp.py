from sre_constants import SUCCESS
from tkinter import Frame
import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('C:\\Users\\darry\\OneDrive\\Dokumen\\GitHub\\Face-Detector-apps\\facedetectorapp\\haarcascade_frontalface_default.xml')

#img = cv2.imread('TS.jpg')
cap = cv2.VideoCapture(0)

while True:
    berhasil, frame = cap.read()

    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    
    for(x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0, 255, 0), 8)

    

    cv2.imshow('facedetector',frame)
    cv2.waitKey(1)






print("Code Complete")
