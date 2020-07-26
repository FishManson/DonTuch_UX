# Demo first phase
# Sergio A. Navarro-Tuch
# Ariel A. Lopez-Aguilar
# 07-24-2020

# Load libraries
import os
import pyautogui	# GUI
import cv2			# OpenCV
import dlib			# Face detection (.dat file needed to run)
import tkinter as tk 
from tkinter import messagebox
import time

class Ball(tk.Canvas):

	def __init__(self):

		super().__init__(width = WIDTH, height = HEIGHT,
						 background = "grey")

		""" DEFINE DOT VARIABLES """
		self.x_center = WIDTH / 2	# Center of screen
		self.y_center = HEIGHT / 2	# Center of screen
		self.RAD = 40				# Dot radious
		self.flag_dot = None		# Is pointer outside dot?
		self.x_pos = self.x_center	# Dot center x
		self.y_pos = self.y_center	# Dot center y
		self.dx = WIDTH // 4		# Divide in 4 parts for ball movement
		self.dy = HEIGHT // 4		# Divide in 4 parts for ball movement
		self.m = (self.y_center - self.dy)	/ (self.x_center - self.dx) # Line ecuation
		self.cont_row = 2			# To move to different place in row

		""" FOLLOW THE DOW """
		self.draw_ball()
		self.pack()
		self.after(1000, self.perform_actions)

	def draw_ball(self):
		ball = self.create_oval(self.x_center - self.RAD, self.y_center - self.RAD,
								self.x_center + self.RAD, self.y_center + self.RAD,
								fill = "red", tag = "ball")

	def perform_actions(self):
		self.move_first_pos()
		self.move_to_next_dot()
		self.move_to_next_dot()
		self.move_to_next_row()
		self.move_to_next_dot()
		self.move_to_next_dot()
		self.move_to_next_row()
		self.move_to_next_dot()
		self.move_to_next_dot()
		self.return_to_center()
		self.move_up()
		self.return_cross()
		self.move_right()
		self.return_cross()
		self.move_down()
		self.return_cross()
		self.move_left()
		self.return_cross()
		messagebox.showinfo('CareToy Attention App', 'Callibration done. Please Esc to close window')
	
	def move_first_pos(self):
		self.x_pos = self.x_center
		self.y_pos = self.y_center
		self.mouse_over_dot()
		if self.flag_dot == True:
			while True:
				if self.x_pos > self.dx:
					self.move("ball", -1, -self.m)
					self.x_pos -= 1
					self.y_pos -= self.m
					self.update()
					time.sleep(0.001)
				else:
					break
		else:
			time.sleep(0.5)
			self.move_first_pos()

	def move_to_next_dot(self):
		self.mouse_over_dot()
		if self.flag_dot == True:
			while True:
				if self.x_pos < self.dx*self.cont_row:
					self.move("ball", 1, 0)
					self.x_pos += 1
					self.update()
					time.sleep(0.001)
				else:
					self.cont_row += 1
					if self.cont_row >= 4:
						self.cont_row = 2
					time.sleep(1)
					break
		else:
			time.sleep(0.5)
			self.move_to_next_dot()


	def move_to_next_row(self):
		self.m = (2 * self.dy - self.dy) / (self.dx - self.x_pos)
		self.mouse_over_dot()
		if self.flag_dot == True:
			while True:
				if self.x_pos > self.dx:
					self.move("ball", -1, -self.m)
					self.x_pos -= 1
					self.y_pos -= self.m
					self.update()
					time.sleep(0.001)
				else:
					time.sleep(1)
					break
		else:
			time.sleep(0.5)
			self.move_to_next_row()

	def return_to_center(self):
		self.m = (self.y_center - self.y_pos) / (self.x_center - self.x_pos)
		self.mouse_over_dot()
		if self.flag_dot == True:
			while True:
				if self.x_pos > self.x_center:
					self.move("ball", -1, -self.m)
					self.x_pos -= 1
					self.y_pos -= self.m
					self.update()
					time.sleep(0.001)
				else:
					time.sleep(1)
					break
		else:
			time.sleep(0.5)
			self.return_to_center()

	def move_up(self):
		self.mouse_over_dot()
		if self.flag_dot == True:
			while True:
				if self.y_pos > self.dy:
					self.move("ball", 0, -1)
					self.y_pos -= 1
					self.update()
					time.sleep(0.001)
				else:
					time.sleep(1)
					break
		else:
			time.sleep(0.5)
			self.move_up()

	def move_right(self):
		self.mouse_over_dot()
		if self.flag_dot == True:
			while True:
				if self.x_pos < self.dx*3:
					self.move("ball", 1, 0)
					self.x_pos += 1
					self.update()
					time.sleep(0.001)
				else:
					time.sleep(1)
					break
		else:
			time.sleep(0.5)
			self.move_up()

	def move_down(self):
		self.mouse_over_dot()
		if self.flag_dot == True:
			while True:
				if self.y_pos < self.dy*3:
					self.move("ball", 0, 1)
					self.y_pos += 1
					self.update()
					time.sleep(0.001)
				else:
					time.sleep(1)
					break
		else:
			time.sleep(0.5)
			self.move_up()

	def move_left(self):
		self.mouse_over_dot()
		if self.flag_dot == True:
			while True:
				if self.x_pos > self.dx:
					self.move("ball", -1, 0)
					self.x_pos -= 1
					self.update()
					time.sleep(0.001)
				else:
					time.sleep(1)
					break
		else:
			time.sleep(0.5)
			self.move_up()

	def return_cross(self):
		self.mouse_over_dot()
		if self.flag_dot == True:
			if self.y_pos == self.dy:
				while True:
					if self.y_pos < self.y_center:
						self.move("ball", 0, 1)
						self.y_pos += 1
						self.update()
						time.sleep(0.001)
					else:
						time.sleep(1)
						break
			elif self.y_pos == self.dy*3:
				while True:
					if self.y_pos > self.y_center:
						self.move("ball", 0, -1)
						self.y_pos -= 1
						self.update()
						time.sleep(0.001)
					else:
						time.sleep(1)
						break
			elif self.x_pos == self.dx:
				while True:
					if self.x_pos < self.x_center:
						self.move("ball", 1, 0)
						self.x_pos += 1
						self.update()
						time.sleep(0.001)
					else:
						time.sleep(1)
						break
			elif self.x_pos == self.dx*3:
				while True:
					if self.x_pos > self.x_center:
						self.move("ball", -1, 0)
						self.x_pos -= 1
						self.update()
						time.sleep(0.001)
					else:
						time.sleep(1)
						break
		else:
			time.sleep(0.5)
			self.return_cross()


	def mouse_over_dot(self):
		self.x, self.y = pyautogui.position()
		if ((self.x_pos - self.RAD > self.x) or (self.x_pos + self.RAD < self.x) or
			(self.y_pos - self.RAD > self.y) or (self.y_pos + self.RAD < self.y)):
			self.flag_dot = False
			#print("Im out")
		else:
			self.flag_dot = True
			#print("Im in")


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


# Follow the dot window
def quitFullScreen(event):
    root.fullScreenState = False
    root.attributes("-fullscreen", root.fullScreenState)
    root.destroy()


root = tk.Tk()							# Create window
WIDTH, HEIGHT = (root.winfo_screenwidth(), root.winfo_screenheight())				# Screen size
root.title('CareToy Attention Tracker')	# Window name
root.resizable(False, False)			# Cant change window size
root.geometry("%dx%d+0+0" % (WIDTH, HEIGHT))	# Window size
root.attributes('-fullscreen', True)
root.fullScreenState = False
root.bind("<Escape>", quitFullScreen)
follow = Ball()							# Create object
follow.pack()							# Merge object

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
		root.mainloop()
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