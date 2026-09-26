import cv2
import numpy as np
import imutils

def color_seg(choice):
    if choice == 'blue':
        lower_hue = np.array([100,30,30])
        upper_hue = np.array([150,148,255])
    elif choice == 'white':
        lower_hue = np.array([0,0,0])
        upper_hue = np.array([0,0,255])
    elif choice == 'black':
        lower_hue = np.array([32,80,0])
        upper_hue = np.array([165,255,49])
    return lower_hue, upper_hue

# define a video capture object
vid = cv2.VideoCapture(0)

while(True):
	
	# Capture the video frame
	# by frame
	ret, frame = vid.read()

	frame = imutils.resize(frame, height = 300)
	chosen_color = 'black'

	# Convert BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# define range of a color in HSV
	lower_hue, upper_hue = color_seg(chosen_color)


	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_hue, upper_hue)

	black=cv2.bitwise_and(frame,frame,mask=mask)

	# Display the resulting frame
	cv2.imshow('frame', frame)

	cv2.imshow('mask', mask)
	
	cv2.imshow('black', black)

	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
