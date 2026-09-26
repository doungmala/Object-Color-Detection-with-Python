import cv2
import numpy as np
import imutils
import RPi.GPIO as GPIO
import time
from time import sleep
from tkinter import *
    
relay_ch = 4

def color_seg(choice):
    if choice == 'blue':
        lower_hue = np.array([97,0,62])
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

def print_something(text):
    print(text)
    
# define a video capture object
vid = cv2.VideoCapture(0)

while(True):
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    frame = imutils.resize(frame, height = 300)
    
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
    if (blacksum>=50):
        # RED ON THEN OFF
        print('Fond black color')
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(relay_ch, GPIO.OUT)
        GPIO.output(relay_ch, GPIO.LOW)
        time.sleep(1)
        GPIO.output(relay_ch, GPIO.HIGH)
        GPIO.cleanup()
    else:
        print('NOT Fond black color')
    
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
    
    
    cv2.imshow('frame', frame)
    cv2.imshow('threshblack', threshblack)
    cv2.imshow('threshblue', threshblue)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
