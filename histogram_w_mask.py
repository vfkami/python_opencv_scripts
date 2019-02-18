from matplotlib import pyplot as plt
import numpy as np 
import argparse
import cv2

def plot_histogram (image, title, mask = None):
	chans = cv2.split(image)
	colors = ("b", "g", "r")
	plt.figure()
	plt.title(title)
	plt.xlabel("Bins")
	plt.ylabel("# of Pixels")

	for (chan, color) in zip(chans, colors):
		hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
		plt.plot(hist, color = color)
		plt.xlim([0, 256])

image = cv2.imread("luffy.jpg") #use always the same image in folder
cv2.imshow("Orginal", image)

plot_histogram(image, "histogram for original image")
mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("applying the mask", masked)

plot_histogram(image, "histogram for masked image", mask = mask)
plt.show()

