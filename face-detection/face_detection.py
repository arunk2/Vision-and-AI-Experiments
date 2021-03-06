import sys
import dlib
from skimage import io
import numpy as np
import cv2

# Usage of HOG algorithm
def hog_detection(file_name):
	# Create a HOG face detector using the built-in dlib class
	face_detector = dlib.get_frontal_face_detector()
	win = dlib.image_window()

	# Load the image into an array
	image = io.imread(file_name)

	# Run the HOG face detector on the image data.
	# The result will be the bounding boxes of the faces in our image.
	faces = face_detector(image, 1)

	# Open a window to show image and face regions marked
	win.set_image(image)
	win.add_overlay(faces)       
	dlib.hit_enter_to_continue()


# Usage of Viola and Jones algorithm
def haar_detection(file_name):
	# Load the haar face and eyes features xml details
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

	img = cv2.imread(file_name)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
	     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	     roi_gray = gray[y:y+h, x:x+w]
	     roi_color = img[y:y+h, x:x+w]
	     eyes = eye_cascade.detectMultiScale(roi_gray)
	     for (ex,ey,ew,eh) in eyes:
		 cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	 
	cv2.imshow('img',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	# Take the image file name from the command line
	if len(sys.argv) != 2:
	    print("Input file is sent as a command line argument. Usage: python face_detection.py <<<<IMAGE_FILE>>>>")
	    exit()
	file_name = sys.argv[1]
	hog_detection(file_name)
	haar_detection(file_name)
