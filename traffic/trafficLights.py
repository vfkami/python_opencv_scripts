from __future__ import print_function
import numpy as np
import cv2

kernel = np.ones((5, 5), np.uint8)

image = cv2.imread("frame2.png")#use always the same image in folder
height, width, channels = image.shape

gray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

edges = cv2.Canny(gray, 50, 500)

cv2.GaussianBlur(gray, (3, 3), 0, gray)

blank_image = np.zeros((height, width, 3), np.uint8)

ret, thresh = cv2.threshold(edges, 127, 255, 0)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = []

for c in contours:
    if len(c) >= 4 | len(c) <= 25:
        cnt.append(c)

cv2.drawContours(blank_image, cnt, -1, (0, 0, 255), 2)

cv2.imshow("image", image)
print(gray)
cv2.imshow("canny", gray)
cv2.imshow("sdas", blank_image)

cv2.waitKey(0)