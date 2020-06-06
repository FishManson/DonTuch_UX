# Sergio A. Navarro-Tuch
# Ariel A. Lopez-Aguilar

# Landmark recognition for UX

import cv2	# OpenCV
import numpy as np
import dlib # Face detection (need .dat file)
# .dat file can be obtained from http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

cap = cv2.VideoCapture(0)	# Video

# Face detection functions from dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Drawing functions for facial landmark
def draw_rectangle(face, img):
	x1 = face.left()
	y1 = face.top()
	x2 = face.right()
	y2 = face.bottom()
	cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

def draw_facepoints(landmarks, img):
	for n in range(0, 68):
		x = landmarks.part(n).x
		y = landmarks.part(n).y
		cv2.circle(img, (x,y), 1, (255, 0, 0), -1)

while True:

	_, frame = cap.read()	# Get frame from webcam
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	# Change to grayscale

	faces = detector(gray)	# Face detection

	n_faces = len(faces)	# Number of faces detected

	if n_faces >= 1:

		for face in faces:

			draw_rectangle(face, frame)	# Draw rectangle for faces

			landmarks = predictor(gray, face)	# Get landmarks

			draw_facepoints(landmarks, frame)	# Draw landmarks points

	else:
		# Print message for No face detection
		h, w, c = frame.shape
		position = (5, h - 10)
		cv2.putText(frame, "NO face detected", position,
			cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

	cv2.imshow("Webcam", frame)

	key = cv2.waitKey(1)
	if key == 27:
		break

cv2.destroyAllWindows()	# Close all windows
