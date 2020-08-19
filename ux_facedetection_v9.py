# Demo first phase
# Sergio A. Navarro-Tuch
# Ariel A. Lopez-Aguilar
# Patch: 08-17-2020
# Patch notes: Mouse cursor now is a transparent eye

# Load libraries
import os
import pyautogui	# GUI to get mouse position
import cv2			# OpenCV
import dlib			# Face detection (.dat file needed to run)
import tkinter as tk 	# Tkinter to build the following track
from tkinter import messagebox
from PIL import Image, ImageTk	# To manipulate the eye object
import time


class Callibration:

	def __init__(self):

		""" FULLSCREEN ATTRIBUTES """
		self.root = tk.Tk()	# Creates root object for interface
		self.root.title("Eye Callibration Test")
		self.root.attributes('-fullscree', True)	# Fullscreen
		self.root.config(cursor = 'none')	# Hide cursor
		self.canvas = tk.Canvas(self.root,
							 width = self.root.winfo_screenwidth(),
							 height = self.root.winfo_screenheight(),
							 background = "grey")
		self.img = Image.open("eye3.png")	# Downlaod png file in the github
		self.img = self.img.resize((180, 96), Image.ANTIALIAS)	# Resize eye image
		self.img = ImageTk.PhotoImage(self.img)	# Convert eye image to tkinter object
		self.cimg = self.canvas.create_image(10, 10, image = self.img)	# Place image in the interface
		
		""" DEFINE RED DOT VARIABLES """
		self.x_center = self.root.winfo_screenwidth() / 2
		self.y_center = self.root.winfo_screenheight() / 2
		self.RAD = 40
		self.flag_dot = None
		self.x_pos = self.x_center
		self.y_pos = self.y_center
		self.dx = self.root.winfo_screenwidth() // 4
		self.dy = self.root.winfo_screenheight() // 4
		self.m = (self.y_center - self.dy)	/ (self.x_center - self.dx) # Line ecuation
		self.cont_row = 2 


		""" ACTIONS """
		self.draw_ball()
		self.canvas.pack()	# Bring all objects to the root
		self.canvas.bind('<Motion>', self.move_eye)	# Eye image follow the mouse pointer
		messagebox.showinfo(message = "Please follow the red circle with your eyes",
							title = "CareInterface")
		self.root.after(1000, self.perform_actions)
		self.root.mainloop()

	""" FUNCTIONS """

	# Eye image track the mouse pointer	
	def move_eye(self, event):
		self.x_eye, self.y_eye = event.x, event.y
		self.canvas.coords(self.cimg, self.x_eye, self.y_eye)

	# Create red dot
	def draw_ball(self):
		ball = self.canvas.create_oval(self.x_center - self.RAD, self.y_center - self.RAD,
										self.x_center + self.RAD, self.y_center + self.RAD,
										fill = "red", tag = "ball")

	def perform_actions(self):
		self.can_i_move()
		self.move_first_pos()
		self.can_i_move()
		for x in range(3):
		 	self.move_dot_row()
		 	self.can_i_move()
		 	self.move_dot_row()
		 	self.can_i_move()
		 	if x < 2:
		 		self.move_next_row()
		self.can_i_move()
		self.move_center()
		self.can_i_move()
		self.move_up()
		self.can_i_move()
		self.return_cross()
		self.can_i_move()
		self.move_right()
		self.can_i_move()
		self.return_cross()
		self.can_i_move()
		self.move_down()
		self.can_i_move()
		self.return_cross()
		self.can_i_move()
		self.move_left()
		self.can_i_move()
		self.return_cross()
		self.root.destroy()

	
	def move_first_pos(self):
		while True:
			if self.x_pos > self.dx:
				self.canvas.move("ball", -1, -self.m)
				self.x_pos -= 1
				self.y_pos -= self.m 
				self.canvas.update()
				time.sleep(0.001)
			else:
				break

	def move_dot_row(self):
		while True:
			if self.x_pos < self.dx * self.cont_row:
				self.canvas.move("ball", 1, 0)
				self.x_pos += 1
				self.canvas.update()
				self.move_image()
				time.sleep(0.001)
			else:
				self.cont_row += 1
				if self.cont_row >= 4:
					self.cont_row = 2
				break

	def move_next_row(self):
		self.m = (2 * self.dy - self.dy) / (self.dx - self.x_pos)
		while True:
			if self.x_pos > self.dx:
				self.canvas.move("ball", -1, -self.m)
				self.x_pos -= 1
				self.y_pos -= self.m
				self.canvas.update()
				time.sleep(0.001)
			else:
				break

	def move_center(self):
		self.m = (self.y_center - self.y_pos) / (self.x_center - self.x_pos)
		while True:
			if self.x_pos > self.x_center:
				self.canvas.move("ball", -1, -self.m)
				self.x_pos -= 1
				self.y_pos -= self.m
				self.canvas.update()
				time.sleep(0.001)
			else:
				break 

	def move_up(self):
		while True:
			if self.y_pos > self.dy:
				self.canvas.move("ball", 0, -1)
				self.y_pos -= 1
				self.canvas.update()
				time.sleep(0.001)
			else:
				break
				
	def move_right(self):
		while True:
			if self.x_pos < self.dx*3:
				self.canvas.move("ball", 1, 0)
				self.x_pos += 1
				self.canvas.update()
				time.sleep(0.001)
			else:
				break

	def move_down(self):
		while True:
			if self.y_pos < self.dy*3:
				self.canvas.move("ball", 0, 1)
				self.y_pos += 1
				self.canvas.update()
				time.sleep(0.001)
			else:
				break

	def move_left(self):
		while True:
			if self.x_pos > self.dx:
				self.canvas.move("ball", -1, 0)
				self.x_pos -= 1
				self.canvas.update()
				time.sleep(0.001)
			else:
				break

	def return_cross(self):
		if self.y_pos == self.dy:
			while True:
				if self.y_pos < self.y_center:
					self.canvas.move("ball", 0, 1)
					self.y_pos += 1
					self.canvas.update()
					time.sleep(0.001)
				else:
					break
		elif self.y_pos == self.dy*3:
			while True:
				if self.y_pos > self.y_center:
					self.canvas.move("ball", 0, -1)
					self.y_pos -= 1
					self.canvas.update()
					time.sleep(0.001)
				else:
					break
		elif self.x_pos == self.dx:
			while True:
				if self.x_pos < self.x_center:
					self.canvas.move("ball", 1, 0)
					self.x_pos += 1
					self.canvas.update()
					time.sleep(0.001)
				else:
					break
		elif self.x_pos == self.dx*3:
			while True:
				if self.x_pos > self.x_center:
					self.canvas.move("ball", -1, 0)
					self.x_pos -= 1
					self.canvas.update()
					time.sleep(0.001)
				else:
					break

	def can_i_move(self):
		while True:
			time.sleep(0.001)
			self.mouse_over_dot()
			if self.flag_dot == True:
				break

	def move_image(self):
		self.get_mouse_coords()
		self.canvas.coords(self.cimg, self.x, self.y)

	def get_mouse_coords(self):
		self.x, self.y = pyautogui.position()

	def mouse_over_dot(self):
		self.get_mouse_coords()
		if ((self.x_pos - self.RAD > self.x) or (self.x_pos + self.RAD < self.x) or
			(self.y_pos - self.RAD > self.y) or (self.y_pos + self.RAD < self.y)):
			self.flag_dot = False
		else:
			self.flag_dot = True



# Get video from camera
cap = cv2.VideoCapture(0)	# Change to 0 if you dont have another webcam

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

Callibration()

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
		pyautogui.alert('New Callibration Needed')
		Callibration()
		cont = 0


# Release webcam
cap.release()

