# -*- coding: utf-8 -*-
"""
Created on Fri Jul  29 18:17:45 2020

@author: Nandita sharma
"""


import cv2
from mtcnn.mtcnn import MTCNN
import os




dire="F_facesscence"

dire1="faces"
os.makedirs(dire1, exist_ok = True)

detector = MTCNN()

def face_detect(path,save):
    image = cv2.imread(path,1)
    result=detector.detect_faces(image)
    if not result:
        print("Their is no any face: ",path)
    if result:
        b=result[0]['box']
        img1=image[b[1]-50:b[1]+b[3]+50,b[0]-50:b[0]+b[2]+50]
        cv2.imwrite(save,img1)
        return(img)
        
for img in os.listdir(dire):
    try:
        path=dire+'/'+img
        save=dire1+"/"+img
        img2=face_detect(path,save)
    except Exception as e:
        print(e)
print("All is done.")
    


