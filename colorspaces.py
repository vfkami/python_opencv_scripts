import numpy as np
import argparse
import imutils
import cv2

##ap = argparse.ArgumentParser()
##ap.add_argument("-i", "--image", required = True,
##	help = "path to the image")
##args = vars(ap.parse_args())

image = cv2.imread("luffy.jpg") #use always the same image in folder
cv2.imshow("Orginal", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
cv2.imshow("L*a*b", lab)

cv2.waitKey(0)