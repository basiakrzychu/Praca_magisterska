#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 22:56:08 2021

@author: basiakrzychu
"""

import cv2

cascade = cv2.CascadeClassifier('/home/basiakrzychu/Documents/magisterka/seminarium/caascade.xml')
cap = cv2.VideoCapture('/home/basiakrzychu/Documents/magisterka/seminarium/filmy/1.mp4')
cap.set(1,321600)  

while 1:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    faces = cascade.detectMultiScale(blur, 1.05,10,minSize=(500,500))

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
   
    cv2.imshow('img',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):     
        break

cap.release()
cv2.destroyAllWindows()