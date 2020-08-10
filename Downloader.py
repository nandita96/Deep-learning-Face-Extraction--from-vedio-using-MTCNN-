# -*- coding: utf-8 -*-
"""
Created on Sat Jul  28 13:33:17 2020

@author: Nandita sharma
"""


from pytube import YouTube
import time
import os
import math
import datetime
import cv2
###############downloading vedio from you tube with url

urlList=["https://www.youtube.com/watch?v=BFMWPejm22w","https://www.youtube.com/watch?v=7ofPYtJP3CE","https://www.youtube.com/watch?v=uZeLseeJdv8"]
start=time.time()
for ind,url in enumerate(urlList):
    try:
        #where to save 
        SAVE_PATH = 'V_comedyScenes'
        yt = YouTube(url)
        print('Title :',yt.title)
        #print('Available formats :')
        #itag = yt.streams.first()
        #stream = yt.streams.first()
        print('\nDownloading--- '+yt.title+' into location : '+SAVE_PATH)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH)
        os.rename('YouTube','YouTube'+str(ind))
        print('!done')
    except Exception as e: 
        print("Error",e) #to handle exception 
        input('Hit Enter to exit')
