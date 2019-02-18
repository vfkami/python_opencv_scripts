from __future__ import print_function
import numpy as np
import argparse
import mahotas
import cv2

image = cv2.imread("coins.png") #use always the same image in folder
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)

edged = cv2.Canny(blurred, 100, 300)
cv2.imshow("Edges", edged)

(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("I count {} coins in this image".format(len(cnts)))

coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)