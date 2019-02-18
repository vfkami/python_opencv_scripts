from __future__ import print_function
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

##ap = argparse.ArgumentParser()
##ap.add_argument("-i", "--image", required = True,
##	help = "path to the image")
##args = vars(ap.parse_args())

image = cv2.imread("luffy.jpg") #use always the same image in folder
cv2.imshow("Orginal", image)


