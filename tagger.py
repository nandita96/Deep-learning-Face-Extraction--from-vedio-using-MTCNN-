# -*- coding: utf-8 -*-
"""
Created on Sat Jul  28 18:19:47 2020

@author: Nandita sharma
"""
import os
import cv2
import matplotlib.pyplot as plt


dire='E:/Labels/vediotofram_emotaion/Nan/faces'
allImages=os.listdir(dire)
category=[]
plt.ion()

for i,image in enumerate(allImages):
    image=cv2.imread(dire+'/'+image,1)
    plt.imshow(image)
    plt.pause(0.05)
    category.append(input('category: '))