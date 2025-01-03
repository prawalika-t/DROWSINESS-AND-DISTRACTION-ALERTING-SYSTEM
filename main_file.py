import cv2
import numpy as np
import time
#import pyttsx
import win32com.client as wincl
from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
from gtts import gTTS
import speech_recognition as sr
import re
import time
import webbrowser
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
import requests
from pygame import mixer
import urllib.request
import urllib.parse
import bs4
import subprocess




#chatbot 
####################################################################################################################


###################################################################################################################
def drowsiness():
        
    #Drosiness Detection
    def eye_aspect_ratio(eye):
        A = distance.euclidean(eye[1], eye[5])
        B = distance.euclidean(eye[2], eye[4])
        C = distance.euclidean(eye[0], eye[3])
        ear = (A + B) / (2.0 * C)
        return ear
        
    thresh = 0.20
    frame_check = 30
    detect = dlib.get_frontal_face_detector()
    predict = dlib.shape_predictor(".\shape_predictor_68_face_landmarks.dat")# Dat file is the crux of the code

    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]



    speak = wincl.Dispatch("SAPI.SpVoice")
    #Load YOLO
    net = cv2.dnn.readNet("yolov3-tiny.weights","yolov3_tiny.cfg") # Original yolov3
    #net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    #net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
    #net = cv2.dnn.readNet("yolov3-tiny.weights","yolov3-tiny.cfg") #Tiny Yolo
    classes = []
    with open("yolov3.txt","r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    outputlayers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    colors= np.random.uniform(0,255,size=(len(classes),3))
    cap=cv2.VideoCapture(0) #0 for 1st webcam
    start_frame_number = 50
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame_number)
    font = cv2.FONT_HERSHEY_PLAIN
    starting_time= time.time()
    frame_id = 0
    flag=0
    while True:
        _,frame= cap.read() # 
        frame_id+=1
        

        frame1 = imutils.resize(frame, width=450)
        gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        subjects = detect(gray, 0)
        for subject in subjects:
            shape = predict(gray, subject)
            shape = face_utils.shape_to_np(shape)#converting to NumPy Array
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            ear = (leftEAR + rightEAR) / 2.0
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame1, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame1, [rightEyeHull], -1, (0, 255, 0), 1)
            if ear < thresh:
                flag += 1
                print (flag)
                if flag >= frame_check:
                    speak.Speak("Please dont get Drowsy while driving")
            else:
                flag=0










        #########################################################################################################################
        #Distraction Dectection
        height,width,channels = frame.shape
        #detecting objects
        blob = cv2.dnn.blobFromImage(frame,0.00392,(320,320),(0,0,0),True,crop=False) #reduce 416 to 320    

            
        net.setInput(blob)
        outs = net.forward(outputlayers)
        #print(outs[1])


        #Showing info on screen/ get confidence score of algorithm in detecting an object in blob
        class_ids=[]
        confidences=[]
        boxes=[]
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.3:
                    #onject detected
                    center_x= int(detection[0]*width)
                    center_y= int(detection[1]*height)
                    w = int(detection[2]*width)
                    h = int(detection[3]*height)

                    #cv2.circle(img,(center_x,center_y),10,(0,255,0),2)
                    #rectangle co-ordinaters
                    x=int(center_x - w/2)
                    y=int(center_y - h/2)
                    #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

                    boxes.append([x,y,w,h]) #put all rectangle areas
                    confidences.append(float(confidence)) #how confidence was that object detected and show that percentage
                    class_ids.append(class_id) #name of the object tha was detected

        indexes = cv2.dnn.NMSBoxes(boxes,confidences,0.4,0.6)


        for i in range(len(boxes)):
            if i in indexes:
                x,y,w,h = boxes[i]
                label = str(classes[class_ids[i]])
                confidence= confidences[i]
                color = colors[class_ids[i]]
                #engine = pyttsx.init()
                if label=="backpack" or label=="handbag" or label=="bottle" or label=="wine glass" or label=="cup" or label=="cell phone" :
                    cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
                    cv2.putText(frame,"alert"+" "+str(round(confidence,2)),(x,y+30),font,1,(255,255,255),2)
                    # engine.say("Please dont use"+str(label)+"while driving")
                    # engine.runAndWait()
                    speak.Speak("Please dont use"+str(label)+"while driving")

                

        elapsed_time = time.time() - starting_time
        fps=frame_id/elapsed_time
        cv2.putText(frame,"FPS:"+str(round(fps,2)),(10,50),font,2,(0,0,0),1)
        
        cv2.imshow("Image",frame)
        key = cv2.waitKey(1) #wait 1ms the loop will start again and we will process the next frame
        
        if key == 27: #esc key stops the process
            break;
        
    cap.release()    
    cv2.destroyAllWindows()
drowsiness()