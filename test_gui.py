import cv2
import numpy as np
import imutils
import RPi.GPIO as GPIO
import time
from time import sleep
import tkinter as tk

import e18_d80nk as e18_d80nk
import time
from tkinter import messagebox

#pin Gpio
pin = 18

#e18_d80nk default gpio High when object detect gpio went low
default_high = True

#Distance
distance_sensor = e18_d80nk.e18_d80nk(pin,default_high)
time.sleep(1)
relay_ch = 4
relay_ch2 = 26

def color_seg(choice):
    if choice == 'blue':
        lower_hue = np.array([97,0,62]) #HSV
        upper_hue = np.array([132,255,253])
    elif choice == 'white':
        lower_hue = np.array([6,0,187])
        upper_hue = np.array([56,39,255])
    elif choice == 'black':
        lower_hue = np.array([92,0,26])
        upper_hue = np.array([173,122,102])
    elif choice == 'yellow':
        lower_hue = np.array([9,112,222])
        upper_hue = np.array([31,247,255])
    elif choice == 'silver':
        lower_hue = np.array([0,0,121])
        upper_hue = np.array([49,72,255])
    return lower_hue, upper_hue

    
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_ch, GPIO.OUT)

def LED3Blink1():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay_ch, GPIO.OUT)
    GPIO.output(relay_ch, GPIO.LOW)
    time.sleep(1)
    GPIO.output(relay_ch, GPIO.HIGH)

def LED3Blink2():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay_ch2, GPIO.OUT)
    GPIO.output(relay_ch2, GPIO.LOW)
    time.sleep(1)
    GPIO.output(relay_ch2, GPIO.HIGH)
                
    #GPIO.cleanup() # this ensures a clean exit 
def print_something(text):
    
    vid = cv2.VideoCapture(0)
    while(True):
        ret, frame = vid.read()
        frame = imutils.resize(frame, height = 300)
        cv2.imshow('frame', frame)
        
            
        if (distance_sensor.get_state() == True):
            print ("Object is detect.")               
            #########################################
            ############# BLACK #####################
            #########################################
            chosen_color = 'black'
            frameblack=frame
            # Convert BGR to HSV
            hsvblack = cv2.cvtColor(frameblack, cv2.COLOR_BGR2HSV)
            # define range of a color in HSV
            lower_hueblack, upper_hueblack = color_seg(chosen_color)
            # Threshold the HSV image to get only blue colors
            maskblack = cv2.inRange(hsvblack, lower_hueblack, upper_hueblack)
                            
            ret,threshblack = cv2.threshold(maskblack,50,255,0)
                            
            blacksum = sum(sum(threshblack))
            print('blacksum',blacksum)
            if (blacksum<=0):
                
                #messagebox.showinfo("Information","Fond black color")
                
                #msg_box = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?',
                  #                      icon='warning')
                #time.sleep(3)
                #msg_box.destroy()
                 
                # RED ON THEN OFF
                print('Fond black color')
               
                LED3Blink1() 
                
                T = tk.Text(app, height=2, width=30)
                T.pack()
                T.insert(tk.END, "Fond black color")
                
                
            else:
                LED3Blink2()
                print('NOT Fond black color')
                #messagebox.showinfo("Information","NOT Fond black color")
            
                T = tk.Text(app, height=2, width=30)
                T.pack()
                T.insert(tk.END, "NOT Fond black color")
                
            #########################################
            ############# BLUE #####################
            #########################################
            chosen_color = 'blue'
            # Convert BGR to HSV
            hsvblue = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # define range of a color in HSV
            lower_hueblue, upper_hueblue = color_seg(chosen_color)
            # Threshold the HSV image to get only blue colors
            maskblue = cv2.inRange(hsvblue, lower_hueblue, upper_hueblue)
                            
            ret,threshblue = cv2.threshold(maskblue,50,255,0)
                            
            bluesum = sum(sum(threshblue))
            print('bluesum',bluesum)
            if (bluesum>=50):
                print('blue')
                            
            #########################################
            ############# WHITE #####################
            #########################################
            chosen_color = 'white'
            # Convert BGR to HSV
            hsvwhite = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # define range of a color in HSV
            lower_huewhite, upper_huewhite = color_seg(chosen_color)
            # Threshold the HSV image to get only blue colors
            maskwhite = cv2.inRange(hsvwhite, lower_huewhite, upper_huewhite)
                            
            ret,threshwhite = cv2.threshold(maskwhite,50,255,0)
                            
            whitesum = sum(sum(threshwhite))
            print('whitesum',whitesum)
            if (whitesum>=50):
                print('white')
                            
            #########################################
            ############# YELLOW #####################
            #########################################
            chosen_color = 'yellow'
            # Convert BGR to HSV
            hsvyellow = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # define range of a color in HSV
            lower_hueyellow, upper_hueyellow = color_seg(chosen_color)
            # Threshold the HSV image to get only blue colors
            maskyellow = cv2.inRange(hsvyellow, lower_hueyellow, upper_hueyellow)
                            
            ret,threshyellow = cv2.threshold(maskyellow,50,255,0)
                            
            yellowsum = sum(sum(threshyellow))
            print('yellowsum',yellowsum)
            if (yellowsum>=50):
                print('yellow')
                            
            #########################################
            ############# SILVER #####################
            #########################################
            chosen_color = 'silver'
            # Convert BGR to HSV
            hsvsilver = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # define range of a color in HSV
            lower_huesilver, upper_huesilver = color_seg(chosen_color)
            # Threshold the HSV image to get only blue colors
            masksilver = cv2.inRange(hsvsilver, lower_huesilver, upper_huesilver)
                            
            ret,threshsilver = cv2.threshold(masksilver,50,255,0)
                            
            silversum = sum(sum(threshsilver))
            print('silversum',silversum)
            if (silversum>=50):
                print('silver')
            
        else:
            print ("Object is not detect.")
       
app = tk.Tk()
app.title("DIGITAL IMAGE PROCESSING")
app.geometry("150x300")

button = tk.Button(text='click me!', command= lambda :print_something('print this'))
#button = tk.Button(text='Exit', command= lambda :Close())
button.pack()
app.mainloop()