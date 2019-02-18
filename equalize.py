from __future__ import print_function
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

image = cv2.imread("luffy.jpg") #use always the same image in folder
cv2.imshow("Orginal", image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(image)

cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
image2 = np.hstack([image, eq])
plt.show()
cv2.waitKey(0)