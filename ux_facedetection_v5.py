# Demo first phase
# Sergio A. Navarro-Tuch
# Ariel A. Lopez-Aguilar
# 07-21-2020

# Load libraries
import os
import pyautogui	# GUI
import cv2			# OpenCV
import dlib			# Face detection (.dat file needed to run)

# Get video from camera
cap = cv2.VideoCapture(1)	# Change to 0 if you dont have another webcam

# Face detection functions from dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


# Get screen resolution
screenW, screenH = pyautogui.size()

# Define Area of Interest (AoI)
scale_AOI = 0.8

AOI_W = int(screenW * scale_AOI)
AOI_H = int(screenH * scale_AOI)

AOI_xstart = int(screenW * ((1 - scale_AOI) / 2))
AOI_xend = int(screenW - (screenW*((1 - scale_AOI) / 2)))
AOI_ystart = int(screenH * ((1 - scale_AOI) / 2))
AOI_yend = int(screenH - (screenH*((1 - scale_AOI) / 2)))


app_flag = True # Flag to initialize game
cont = 0 # Cont to alert user

while True:

	# Get frame from webcam
	_, frame = cap.read()

	# Transforms to grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Look for faces in the frame
	faces = detector(gray)

	# Number of faces detected
	n_faces = len(faces)

	# If no face is detected
	if n_faces < 1:
		# Display message for no face detected
		pyautogui.alert('Hey! Look at the screen!')
		cont += 1

	# Initialize the game
	if app_flag == True:
		os.startfile("C:/Users/Fish/Documents/DCI/FebJun2020/UX/Care interface_ Eliu Castillo A01121561/CareInterface.exe")
		app_flag = False

	mouse_x, mouse_y = pyautogui.position()	# Gets AoI

	# Is pointer in AoI?
	if (mouse_x < AOI_xstart or mouse_x > AOI_xend or mouse_y < AOI_ystart or mouse_y > AOI_yend):
		# Disaplay message i user is not paying attention
		pyautogui.alert('PAY ATENTION!')
		# If cont > 5, it stops looking for user
		cont += 1

	if cont >= 5:
		break

# Release webcam
cap.release()



