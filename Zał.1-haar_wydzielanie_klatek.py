#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 00:02:09 2021

@author: basiakrzychu
"""

import cv2

numer="1" #nazwa pliku wideo
isPostive=1 #pozytywne czy negatywne

cap=cv2.VideoCapture('/home/basiakrzychu/Documents/magisterka/seminarium/filmy/'+str(numer)+'.mp4')
totalframecount= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Ilośc klatek w filmie ",numer,": ", totalframecount,sep="")
i=400 #początkowa klatka
p=100 #co która klatka

while(cap.isOpened()):
    cap.set(1,i)
    ret, frame = cap.read() 
    
    if ret==False:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    cv2.imshow('frame', frame)
    if isPostive==True:   
        cv2.imwrite('/home/basiakrzychu/Documents/magisterka/seminarium/positives/'+str(numer)+'_'+str(i)+'.jpg',blur)
    else:
        cv2.imwrite('/home/basiakrzychu/Documents/magisterka/seminarium/negatives/'+str(numer)+'_'+str(i)+'.jpg',blur)
    i+=p;
    if cv2.waitKey(1) & 0xFF == ord('q'):     
        break

cap.release()
cv2.destroyAllWindows()