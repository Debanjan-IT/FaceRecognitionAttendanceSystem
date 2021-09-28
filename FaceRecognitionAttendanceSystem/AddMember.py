from tkinter import messagebox
import os


def createDir(name):
	parent_dir = "image/"
	path = os.path.join(parent_dir, name)
	os.mkdir(path)
	messagebox.showinfo("Notification", "Member Added. Press 'OK' to capture photos.")
	return path


def start(name):
	if len(name) > 0:
		path = createDir(name)
		import cv2
		cap = cv2.VideoCapture(0)
		i = 0
		while(i < 10):
			ret, frame = cap.read()
			if ret == False:
				break
			cv2.imwrite(path+'/img'+str(i)+'.jpg', frame)
			i += 1
		return True