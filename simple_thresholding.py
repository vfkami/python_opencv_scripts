import numpy as np
import argparse
import cv2

image = cv2.imread("mini_john.png") #use always the same image in folder
cv2.imshow("Orginal", image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("threshold Binary", thresh)

(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("threshold Binary Inverse", threshInv)

cv2.imshow("Coins", cv2.bitwise_and(image, image, mask = threshInv))
cv2.waitKey(0)