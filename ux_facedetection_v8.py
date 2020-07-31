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
import time

class Callibration:

	def __init__(self):

		""" FULLSCREEN ATTRIBUTES """
		self.root = tk.Tk()
		self.root.title("Callibration")
		self.root.attributes('-fullscreen', True)
		self.canvas1 = tk.Canvas(self.root,
								 width = self.root.winfo_screenwidth(),
								 height = self.root.winfo_screenheight(),
								 background = "grey")

		""" DEFINE DOT VARIABLES """
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
		self.mouse_dot()
		self.draw_ball()
		self.canvas1.pack()
		self.root.after(1000, self.perform_actions)
		self.root.mainloop()

	""" FUNCTIONS FOR ACTIONS """
	def draw_ball(self):
		ball = self.canvas1.create_oval(self.x_center - self.RAD, self.y_center - self.RAD,
										self.x_center + self.RAD, self.y_center + self.RAD,
										fill = "red", tag = "ball")

	def perform_actions(self):
		self.move_first_pos()
		time.sleep(1)
		for x in range(3):
			self.move_dot_row()
			self.move_dot_row()
			if x < 2:
				self.move_next_row()
		self.move_center()
		self.move_up()
		self.return_cross()
		self.move_right()
		self.return_cross()
		self.move_down()
		self.return_cross()
		self.move_left()
		self.return_cross()
		time.sleep(0.5)
		self.root.destroy()

	def move_first_pos(self):
		self.mouse_dot()
		if self.flag_dot == True:
			while True:
				if self.x_pos > self.dx:
					self.canvas1.move("ball", -1, -self.m)
					self.x_pos -= 1
					self.y_pos -= self.m
					self.canvas1.update()
					time.sleep(0.001)
				else:
					break
		else:
			time.sleep(0.5)
			self.move_first_pos()

	def move_dot_row(self):
		self.mouse_dot()
		if self.flag_dot == True:
			while True:
				if self.x_pos < self.dx*self.cont_row:
					self.canvas1.move("ball", 1, 0)
					self.x_pos += 1
					self.canvas1.update()
					time.sleep(0.001)
				else:
					self.cont_row += 1
					if self.cont_row >= 4:
						self.cont_row = 2
					time.sleep(1)
					break
		else:
			time.sleep(0.5)
			self.move_dot_row()

	def move_next_row(self):
		self.m = (2 * self.dy - self.dy) / (self.dx - self.x_pos)
		self.mouse_dot()
		if self.flag_dot == True:
			while True:
				if self.x_pos > self.dx:
					self.canvas1.move("ball", -1, -self.m)
					self.x_pos -= 1
					self.y_pos -= self.m
					self.canvas1.update()
					time.sleep(0.001)
				else:
					time.sleep(1)
					break
		else:
			time.sleep(0.5)
			self.move_next_row()

	def move_center(self):
		self.m = (self.y_center - self.y_pos) / (self.x_center - self.x_pos)
		self.mouse_dot()
		if self.flag_dot == True:
			while True:
				if self.x_pos > self.x_center:
					self.canvas1.move("ball", -1, -self.m)
					self.x_pos -= 1
					self.y_pos -= self.m
					self.canvas1.update()
					time.sleep(0.001)
				else:
					time.sleep(1)
					break
		else:
			time.sleep(0.5)
			self.move_center()

	def move_up(self):
		self.mouse_dot()
		if self.flag_dot == True:
			while True:
				if self.y_pos > self.dy:
					self.canvas1.move("ball", 0, -1)
					self.y_pos -= 1
					self.canvas1.update()
					time.sleep(0.001)
				else:
					time.sleep(1)
					break
		else:
			time.sleep(0.5)
			self.move_up()

	def move_right(self):
		self.mouse_dot()
		if self.flag_dot == True:
			while True:
				if self.x_pos < self.dx*3:
					self.canvas1.move("ball", 1, 0)
					self.x_pos += 1
					self.canvas1.update()
					time.sleep(0.001)
				else:
					time.sleep(1)
					break
		else:
			time.sleep(0.5)
			self.move_right()

	def move_down(self):
		self.mouse_dot()
		if self.flag_dot == True:
			while True:
				if self.y_pos < self.dy*3:
					self.canvas1.move("ball", 0, 1)
					self.y_pos += 1
					self.canvas1.update()
					time.sleep(0.001)
				else:
					time.sleep(1)
					break
		else:
			time.sleep(0.5)
			self.move_down()

	def move_left(self):
		self.mouse_dot()
		if self.flag_dot == True:
			while True:
				if self.x_pos > self.dx:
					self.canvas1.move("ball", -1, 0)
					self.x_pos -= 1
					self.canvas1.update()
					time.sleep(0.001)
				else:
					time.sleep(1)
					break
		else:
			time.sleep(0.5)
			self.move_left()

	def return_cross(self):
		self.mouse_dot()
		if self.flag_dot == True:
			if self.y_pos == self.dy:
				while True:
					if self.y_pos < self.y_center:
						self.canvas1.move("ball", 0, 1)
						self.y_pos += 1
						self.canvas1.update()
						time.sleep(0.001)
					else:
						time.sleep(1)
						break
			elif self.y_pos == self.dy*3:
				while True:
					if self.y_pos > self.y_center:
						self.canvas1.move("ball", 0, -1)
						self.y_pos -= 1
						self.canvas1.update()
						time.sleep(0.001)
					else:
						time.sleep(1)
						break
			elif self.x_pos == self.dx:
				while True:
					if self.x_pos < self.x_center:
						self.canvas1.move("ball", 1, 0)
						self.x_pos += 1
						self.canvas1.update()
						time.sleep(0.001)
					else:
						time.sleep(1)
						break
			elif self.x_pos == self.dx*3:
				while True:
					if self.x_pos > self.x_center:
						self.canvas1.move("ball", -1, 0)
						self.x_pos -= 1
						self.canvas1.update()
						time.sleep(0.001)
					else:
						time.sleep(1)
						break
		else:
			time.sleep(0.5)
			self.return_cross()

	def mouse_dot(self):
		self.x, self.y = pyautogui.position()
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


display = Callibration()


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
		display = Callibration()
		cont = 0


# Release webcam
cap.release()