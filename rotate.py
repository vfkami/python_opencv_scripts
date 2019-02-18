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

(h, w) = image.shape[:2]
center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine (image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)

M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)
cv2.waitKey(0)