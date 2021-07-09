import cv2
import numpy as np
from imutils import resize
from pygame import mixer 
mixer.init()
cap=cv2.VideoCapture(0)
p1=0
p2=0
alpha=0.4
while True:
      
      _, frame= cap.read()
      hsv_frame= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
      bassim=cv2.imread("bass.png")
      bim=resize(bassim,width=200,height=200)
      snareim=cv2.imread("snare.png")
      sim=resize(snareim,width=200,height=200)
      low_black = np.array([0,0,0])
      high_black = np.array([350,355 ,100 ])
      black_mask = cv2.inRange(hsv_frame  ,  low_black,  high_black)
      black = cv2.bitwise_and(frame , frame , mask=black_mask)
      bbcheck=black[250:450,15:215]
      sbcheck=black[250:450,420:620]
      added_image1 = cv2.addWeighted(frame[250:450,15:215,:],alpha,bim[0:200,0:200,:],1-alpha,0)
      added_image2 = cv2.addWeighted(frame[250:450,420:620,:],alpha,sim[0:200,0:200,:],1-alpha,0)
      frame[250:450,15:215] = added_image1
      frame[250:450,420:620] = added_image2
      cv2.imshow('Virtual Drum',frame)
      if np.average(bbcheck)>=10 and p1==0 and p2==0:
          mixer.music.load('basssound.ogg')
          mixer.music.play()
          p1=1
      if np.average(bbcheck)<10 and p1==1:
          mixer.music.stop()
          p1=0 
      if np.average(sbcheck)>=10 and p2==0 and p1==0:
          mixer.music.load('snaresound.ogg')
          mixer.music.play()
          p2=1
      if np.average(sbcheck)<10 and p2==1:
          mixer.music.stop()
          p2=0         
      key= cv2.waitKey(1)
      if key == ord('q'):
        break





