# Demo first phase
# Sergio A. Navarro-Tuch
# Ariel A. Lopez-Aguilar
# 07-23-2020

# Load libraries
import os
import pyautogui	# GUI
import cv2			# OpenCV
import dlib			# Face detection (.dat file needed to run)
import tkinter as tk 
import time

# Define class for follow dot section
class Ball(tk.Canvas):
	# The Canvas is a rectangular area intended for drawing pictures or other complex layouts. 
	# You can place graphics, text, widgets or frames on a Canvas.
	global root

	def __init__(self):
		super().__init__(width = WIDTH, height = HEIGHT, background = "grey")

		# Define center to place dot
		self.x_center = WIDTH / 2
		self.y_center = HEIGHT / 2
		self.rad = 40

		self.initialize_ball()

		self.pack(side = "top")

		# Divide the screen in 16 parts (4x4) to place the ball in 9 places
		self.dx = WIDTH //  4
		self.dy = HEIGHT // 4

		# Line ecuation
		self.m = (self.y_center - self.dy) / (self.x_center - self.dx)

		# Move ball to first position
		self.move_to_first_pos()

		# Define ball sequence
		self.move_through_row()
		self.move_to_next_row()
		self.move_through_row()
		self.move_to_next_row()
		self.move_through_row()
		

	def initialize_ball(self):
		ball = self.create_oval(self.x_center - self.rad, self.y_center - self.rad,
								self.x_center + self.rad, self.y_center + self.rad,
								fill = "red", tag = "ball")

	def move_to_first_pos(self):
		self.x_pos = self.x_center
		self.pause_flag = True
		while True:
			if self.x_pos >= self.dx:
				self.move("ball", -1, -self.m)
				self.x_pos -= 1
				self.update()
				time.sleep(0.001)
				if self.pause_flag == True:
					time.sleep(5)
					self.pause_flag = False
			else:
				time.sleep(1)
				break

	def move_through_row(self):
		for x in range(2, 4):
			time.sleep(1)
			while True:
				if self.x_pos < self.dx*x:
					self.move("ball", 1, 0)
					self.x_pos += 1
					self.update()
					time.sleep(0.001)
				else:
					time.sleep(1)
					break

	def move_to_next_row(self):

		self.m = (2 * self.dy - self.dy) / (self.dx - self.x_pos)
		print(self.x_pos)
		time.sleep(1)

		while True:
			if self.x_pos > self.dx:
				self.move("ball", -1, -self.m)
				self.x_pos -= 1
				self.update()
				time.sleep(0.001)
			else:
				print(self.x_pos)
				time.sleep(1)
				break

	def close_callibration(self):
		self.after(1000, lambda: self.destroy())


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

# Initialize gaze callibration

root = tk.Tk()

WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

root.title('CareToy Attention Tracker')
root.resizable(False, False)
root.geometry("%dx%d+0+0" % (WIDTH, HEIGHT))
follow = Ball()
follow.pack()

root.after(1000, lambda: root.destroy())
root.mainloop()

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