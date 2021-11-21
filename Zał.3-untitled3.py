#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 13:08:26 2021

@author: basiakrzychu
"""


import cv2

numer="9" #nazwa pliku wideo


cap=cv2.VideoCapture('D:/magisterka/filmy/'+str(numer)+'.mp4')
totalframecount= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Ilośc klatek w filmie ",numer,": ", totalframecount,sep="")
i=100 #początkowa klatka
p=100 #co która klatka

while(cap.isOpened()):
    cap.set(1,i)
    ret, frame = cap.read() 
    
    if ret==False:
        break
    cv2.imshow('frame', frame)
    
    cv2.imwrite('D:/magisterka/color/'+str(numer)+'_'+str(i)+'.jpg',frame)
    i+=p;
    if cv2.waitKey(1) & 0xFF == ord('q'):     
        break

cap.release()
cv2.destroyAllWindows()