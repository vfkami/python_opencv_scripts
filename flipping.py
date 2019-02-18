import numpy as np
import argparse
import imutils
import cv2

##ap = argparse.ArgumentParser() #use diffrent image
##ap.add_argument("-i", "--image", required = True,
##	help = "path to the image")
##args = vars(ap.parse_args())

image = cv2.imread("john1.jpg") #use always the same image in folder
cv2.imshow("Orginal", image)

flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally and Vertically", flipped)

cv2.waitKey(0)