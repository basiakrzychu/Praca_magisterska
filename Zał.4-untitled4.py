# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 21:55:27 2021

@author: basiakrzychu
"""

import cv2

numer="3" #nazwa pliku wideo


cap=cv2.VideoCapture('D:/magisterka/filmy/'+str(numer)+'.mp4')

totalframecount= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Ilośc klatek w filmie ",numer,": ", totalframecount,sep="")

font = cv2.FONT_HERSHEY_SIMPLEX
org = (250, 250)
fontScale = 5
color = (255, 255, 255)
color2 = (0, 0, 0)
thickness = 10

godzina=2
minuta=51
sekunda=10
czas=sekunda*1000+minuta*60*1000+godzina*60*60*1000
while(cap.isOpened()):
    
    cap.set(cv2.CAP_PROP_POS_MSEC,czas)  
    ret, frame = cap.read() 
    if ret==False:
        break

    i=int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    cv2.imwrite('D:/magisterka/color/'+str(numer)+'_'+str(i)+'.jpg',frame)
    
    image = cv2.putText(frame, str(i), org, font, fontScale, color, thickness+5, cv2.LINE_AA)
    image = cv2.putText(frame, str(i), org, font, fontScale, color2, thickness, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):     
        break    
cap.release()
cv2.destroyAllWindows()
