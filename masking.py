import numpy as np
import argparse
import cv2

##ap = argparse.ArgumentParser()
##ap.add_argument("-i", "--image", required = True,
##	help = "path to the image")
##args = vars(ap.parse_args())

image = cv2.imread("luffy.jpg") #use always the same image in folder
cv2.imshow("Orginal", image)

mask = np.zeros(image.shape[:2], dtype = "uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)

cv2.rectangle(mask, (cX - 90, cY - 90), (cX + 90, cY + 90), 255, -1)
cv2.imshow("Mask", mask)
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask Applied to Image", masked)

mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.circle(mask, (cX, cY), 100, 255, -1)
cv2.imshow("mask2", mask)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask applied to image 2", masked)
cv2.waitKey(0)