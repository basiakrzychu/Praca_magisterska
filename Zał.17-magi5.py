# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 16:14:35 2021

@author: basiakrzychu
"""

import os
from IPython.display import Image, display
from keras.preprocessing.image import load_img
import PIL
from PIL import ImageOps
from tensorflow import keras
import numpy as np
from tensorflow.keras import layers
import tensorflow as tf
import random
from keras_preprocessing import image
import cv2
import time
import matplotlib.pyplot as plt

model = keras.models.load_model("modele/model_144_256.h5",compile=False)
model.load_weights('wagi10.h5')

def display_mask4(xd2):
    """Quick utility to display a model's prediction."""
    mask = np.argmax(xd2[0], axis=-1)
    mask = np.expand_dims(mask, axis=-1)
    img = PIL.ImageOps.autocontrast(keras.preprocessing.image.array_to_img(mask))
    img2=np.array(img)   

    return img2

numer=3
cap=cv2.VideoCapture('D:/magisterka/filmy/'+str(numer)+'.mp4')
totalframecount= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
klatka=328000
cap.set(1,klatka)

while 1:
    
    ret, frame = cap.read()
    if ret == True:
        resized_frame = cv2.resize(frame,(256,144),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        resized_frame2 = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
    else:
        break
    haha4=np.array(resized_frame2)
    haha5=haha4.reshape(1,144,256,3)
    xd2=model.predict(haha5,batch_size=1)
    
    img2= display_mask4(xd2) 
    img2[img2==255]=1
    img2[img2==0]=254
    img2[img2==127]=0
    img3=img2+1
    img3[img3==2]=254
    
    img4=cv2.merge((img3,img2,img3))
    alpha=0.7
    beta = (1.0 - alpha)
    img5 = cv2.addWeighted(resized_frame, alpha, img4, beta, 0.0)
    img6=cv2.resize(img4,(1920,1080),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
    img7 = cv2.addWeighted(frame, alpha, img6, beta, 0.0)
    cv2.imshow('xd',img7)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):     
        break

cap.release()
cv2.destroyAllWindows()

