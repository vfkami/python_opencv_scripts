import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype = "uint8")

red = (0, 0, 255)
blue = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

cv2.line(canvas, (0, 0), (300, 300), green)
##cv2.imshow("Canvas", canvas)
##cv2.waitKey(0)

cv2.line(canvas, (300, 0), (0, 300), red, 5)
##cv2.imshow("canvas", canvas)
##cv2.waitKey(0)

cv2.rectangle(canvas, (10, 10), (60,60), green)
##cv2.imshow("Canvas", canvas)
##cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), blue, 3)
##cv2.imshow("Canvas", canvas)
##cv2.waitKey(0)

cv2.rectangle(canvas, (200, 50), (255, 125), red, -1)
cv2.imshow("retangle canvas", canvas)
cv2.waitKey(0)

canvas2 = np.zeros((300, 300, 3), dtype = "uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)

cv2.circle(canvas2, (centerX, centerY), 50, white, -1)

cv2.imshow("circle canvas", canvas2)
cv2.waitKey(0)
