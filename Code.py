# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 19:43:39 2018

@author: Shri Krishn 
"""

import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
#use it for best result for open and closed 
eye_cascade_open_right = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
#use it for only open 
eye_cascade_open = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_mcs_lefteye.xml')
#cap = cv2.VideoCapture('testing.MKV')
cap = cv2.VideoCapture(0)
#while (cap.isOpened()):
left = [0] * 10
right = [0] * 10
while 1:
     ret, img = cap.read()
     img = cv2.flip(img,1)
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
     face_length = len(faces)
    
     if face_length>0:
      for (x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(145,100,0),3)
       
       #pyautogui.moveTo(x+w/2,y+h/2)
       
       img_right = img[y:y+(h*3/4),x:x+(w/2)]  
       img_left =  img[y:y+(h*3/4),x + (w/2):x+(w)]  
       gray_right = gray[y:y+(h*3/4),x:x+(w/2)] 
       gray_left = gray[y:y+(h*3/4),x + (w/2):x+(w)]  
     
       eyes_open_right = eye_cascade_open.detectMultiScale(gray_right)
       eyes_right = eye_cascade.detectMultiScale(gray_right)
       eye_length_open_right = len(eyes_open_right)
       eye_length_right = len(eyes_right)
     
       eyes_open_left = eye_cascade_open.detectMultiScale(gray_left)
       eyes_left = eye_cascade.detectMultiScale(gray_left)
       eye_length_open_left = len(eyes_open_left)
       eye_length_left = len(eyes_left)
     
       if eye_length_right > 0 and eye_length_open_right==0 and eye_length_open_left > 0:
        
         left.pop()
         left.insert(0,1)
         print "RIght_CLick",eye_length_open_right , eye_length_right
       else :
         left.pop()
         left.insert(0,0)
         print "Eye is open",eye_length_open_right,  eye_length_right
         
       if eye_length_left > 0 and eye_length_open_left==0 and eye_length_open_right > 0:
        
         right.pop()
         right.insert(0,1)
         print "Left_CLick",eye_length_open_left , eye_length_left
       else :
         right.pop()
         right.insert(0,0)
         print "Eye is open",eye_length_open_left,  eye_length_left    
        # print eye_length_open
     
       print "left_sum = ",sum(left),"right_sum = ", sum(right)
       if sum(right) > 5 and sum(left) <5:
            cv2.putText(img, "Right_click" ,(400, 30),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            right = [0]*10
       if sum(left) > 5 and sum (right) < 5:
            cv2.putText(img, "Left_click", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            left = [0] * 10
       
           
       
       for (ex,ey,ew,eh) in eyes_open_left:
        cv2.rectangle(img_left,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)     
       for (ex,ey,ew,eh) in eyes_open_right:
        cv2.rectangle(img_right,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)  
     cv2.imshow("img",img)

     k = cv2.waitKey(1) & 0xff
     if k == 27:
        break  
cap.release()
cv2.destroyAllWindows()     
