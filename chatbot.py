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
import os
def chatbot():
    def talk(audio):
        "speaks audio passed as argument"
        count=0
        print(audio)
        for line in audio.splitlines():
            count+=1
            text_to_speech = gTTS(text=audio, lang='en-uk')
            text_to_speech.save('audio'+str(count)+'.mp3')
            mixer.init()
            mixer.music.load('audio'+str(count)+'.mp3')
            mixer.music.play()
            #os.remove("audio.mp3")

    def play(path):
        mixer.init()
        mixer.music.load(path)#'D:/Final_Year_Project/New_Approch/YOLO/object-detection-opencv-master/1.mp3.mp3')
        mixer.music.play()


    def myCommand():
        "listens for commands"
        #Initialize the recognizer
        #The primary purpose of a Recognizer instance is, of course, to recognize speech. 
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print('TARS is Ready...')
            r.pause_threshold = 1
            #wait for a second to let the recognizer adjust the  
            #energy threshold based on the surrounding noise level 
            r.adjust_for_ambient_noise(source, duration=1)
            #listens for the user's input
            audio = r.listen(source)
            print('analyzing...')

        try:
            command = r.recognize_google(audio).lower()
            print('You said: ' + command + '\n')
            time.sleep(2)

        #loop back to continue to listen for commands if unrecognizable speech is received
        except sr.UnknownValueError:
            print('Your last command couldn\'t be heard')
            command = myCommand();

        return command


    def tars(command):
        errors=[
            "I don't know what you mean",
            "Excuse me?",
            "Can you repeat it please?",
        ]
        "if statements for executing commands"

        
        #Send Email
        
        if 'play music'== command:
            play("D:/Final_Year_Project/New_Approch/YOLO/object-detection-opencv-master/1.mp3.mp3")
        elif 'stop music' in command:
            print("Stopping.....")
            ''' mixer.music.unload('D:/Final_Year_Project/New_Approch/YOLO/object-detection-opencv-master/1.mp3.mp3')'''
            play("D:/Final_Year_Project/New_Approch/YOLO/object-detection-opencv-master/text.mp3")
        if 'hello' in command or 'hi' in command:
            print("Hello ! How are you doing")
            play("D:/Final_Year_Project/New_Approch/YOLO/object-detection-opencv-master/hello.mp3")
        if 'tell me a fact' in command:
            print("The Spanish national anthem has no words.")
            play("D:/Final_Year_Project/New_Approch/YOLO/object-detection-opencv-master/fact1.mp3")
            
        

            
            
        
        


    talk('TARS activated!')

    #loop to continue executing multiple commands
    i=0
    while i<10:
        i+=1
        time.sleep(4)
        tars(myCommand())
chatbot()
    



