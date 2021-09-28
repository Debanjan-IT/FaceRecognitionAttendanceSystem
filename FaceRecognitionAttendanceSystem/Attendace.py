from skimage.metrics import structural_similarity as ssim
import datetime 
import numpy as np
import mysql.connector
from tkinter import messagebox
from tkinter import *
import os
import cv2


def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	return err
def compare_images(imageA, imageB, max):
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB, multichannel=True)
	if max < s:
		max = s
		return max
	else:
		return max


def main(path):
	images = os.listdir(path)
	max = 0
	cap = cv2.VideoCapture(0)
	i = 0
	while(i < 1):
		ret, frame = cap.read()
		if ret == False:
			break
		cv2.imwrite('test.jpg', frame)
		i += 1
	for j in images:
		img1 = cv2.imread("test.jpg")
		filepath = path+'/'+j
		img = cv2.imread(filepath)
		max = compare_images(img1,img, max)
	return max



def start(name):
	if len(name) > 0:
		path = 'image/'+name
		max = main(path)
		if max > 0.5:
			messagebox.showinfo("Notification", "User Matched. Press OK")
			mydb = mysql.connector.connect(
				host="localhost",
				user="root",
				password="",
				database="attendance"
			)
			current_time = datetime.datetime.now() 
			year = current_time.year
			month = current_time.month
			day = current_time.day
			date = str(year) +'-'+str(month)+'-'+str(day)
			mycursor = mydb.cursor()
			sql = "INSERT INTO attendance (member_name,date) VALUES (%s,%s)"
			val = (name,date)
			mycursor.execute(sql, val)
			mydb.commit()
			return True
		else:
			return False
		