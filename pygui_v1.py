import os
import pyautogui

#screenW = pyautogui.size()[0]
#screenH = pyautogui.size()[1]

screenW, screenH = pyautogui.size()

#print("Width: {0}, Height: {1}".format(screenW, screenH))

# Define Area of Interest (AoI)

scale_AOI = 0.8

AOI_W = int(screenW * scale_AOI)
AOI_H = int(screenH * scale_AOI)

AOI_xstart = int(screenW * ((1 - scale_AOI) / 2))
AOI_xend = int(screenW - (screenW*((1 - scale_AOI) / 2)))
AOI_ystart = int(screenH * ((1 - scale_AOI) / 2))
AOI_yend = int(screenH - (screenH*((1 - scale_AOI) / 2)))


app_flag = True
suma = 0

while True:

	if app_flag == True:
		os.startfile("C:/Users/Fish/Documents/DCI/FebJun2020/UX/Care interface_ Eliu Castillo A01121561/CareInterface.exe")
		app_flag = False

	mouse_x, mouse_y = pyautogui.position()

	if (mouse_x < AOI_xstart or mouse_x > AOI_xend or mouse_y < AOI_ystart or mouse_y > AOI_yend):
		pyautogui.alert('PAY ATENTION!')
		suma += 1
	#else:
		#pass

	if suma >= 5:
		break

