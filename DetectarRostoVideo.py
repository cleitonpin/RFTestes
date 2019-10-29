import numpy as np
import cv2
from google_images_download import google_images_download   #importing the library

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cont = 0
while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
    cv2.imshow("frame", gray)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w, y+h), (255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
           
        if roi_gray.all():
            n = 1
            while n > 0:
                #print(n)
                n = n + 1
                cv2.imwrite("train/Foto."+ str(cont) + ".jpg", roi_gray)
                cv2.waitKey(300)
                cv2.imshow("foto capturada", roi_gray)

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew, ey+eh), (255,0,0),2)
        
    
    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)

    if key == 27:
        exit()
    
cap.release()
cv2.destroyAllWindows()