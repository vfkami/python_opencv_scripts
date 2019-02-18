import numpy as np
import argparse
import imutils
import cv2

##ap = argparse.ArgumentParser()
##ap.add_argument("-i", "--image", required = True,
##	help = "path to the image")
##args = vars(ap.parse_args())

image = cv2.imread("john1.jpg") #use always the same image in folder
cv2.imshow("Orginal", image)

cropped = image[100:200, 100:200]
cv2.imshow("image cropped", cropped)
cv2.waitKey(0)