import matplotlib.pyplot as plt
import numpy as np
import cv2

# Instances the image, converts the color to hsv and applies the bilateralFilter
image = cv2.imread("frame.png")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
blur = cv2.bilateralFilter(hsv, 13, 30, 30)

# Set as color boundaries and perform border search of the traffic light
boundaries = [([0, 0, 110], [240, 100, 255])]
kernel = np.ones((2, 2), np.uint8)

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    mask = cv2.inRange(blur, lower, upper)

    output = cv2.bitwise_and(blur, blur, mask=mask)
    output_gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)

# Find edges with canny and apply morphological treatments
edged = cv2.Canny(output_gray, 150, 400)
edged = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
edged = cv2.dilate(edged, kernel, iterations=1)

# find contours
_, contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

rectangleContours = []

# Rectangularity Test
for c in contours:
    epsilon = 0.05 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)

    if len(approx) == 4:  ## filter array for only 4 points
        if cv2.contourArea(approx) > 500:  ## filter small contours
            if cv2.isContourConvex(approx) == True:  ## filter if contour is convex
                rectangleContours.append(approx)

# Limit of traffic light colors

                   #b  #g  #r      #b   #g   #r
greenBoundaries = [([70, 170, 10], [255, 255, 174])]
redBoundaries = [([5, 35, 225], [70, 135, 255])]
yellowBoundaries = [([5, 230, 230], [32, 255, 255])]
##^ code ok ^##

# crop the images and search the colors
clusters = 10


for c in rectangleContours:
    x, y, a, b = cv2.boundingRect(c)
    img_cropped = image[y:y + b, x:x + a]

    #kmeans
    Z = img_cropped.reshape((-1, 3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

    epsilon = 0.05 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)

    K = 7
    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img_cropped.shape))

    for (lower, upper) in greenBoundaries:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        greenMask = cv2.inRange(res2, lower, upper)

    for (lower, upper) in yellowBoundaries:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        yellowMask = cv2.inRange(res2, lower, upper)

    for (lower, upper) in redBoundaries:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        redMask = cv2.inRange(res2, lower, upper)

    finalMask = redMask + yellowMask + greenMask
    output = cv2.bitwise_and(res2, res2, mask=finalMask)

    output_edge = cv2.Canny(output, 150, 400)
    output_edge = cv2.dilate(output_edge, kernel, iterations=2)

    _, contours, _ = cv2.findContours(output_edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    circleContours = []

    for c in contours:
        epsilon = 0.05 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)

        if len(approx) > 4:  ## filter array for only 4 points
            if cv2.contourArea(approx) > 15:  ## filter small contours
                if cv2.isContourConvex(approx) == True:  ## filter if contour is convex
                    circleContours.append(approx)

                    # compute the center of the contour
                    M = cv2.moments(c)
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])

                    # draw the contour and center of the shape on the image
                    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
                    cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
                    cv2.putText(image, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

        cv2.imshow("image", img_cropped)
        cv2.waitKey(0)

    #cv2.rectangle(image, (x, y), (x + a, y + b), (0, 255, 0), 2)
    #cv2.drawContours(image, rectangleContours, -1, (0, 0, 255), 1)



#cv2.rectangle(image, (x, y), (x + a, y + b), (0, 255, 0), 2)

#cv2.line(image, (x, y), (x, yend), (0, 0, 255), 5)
#cv2.drawContours(image, rectangleContours, -1, (0, 0, 255), 1)

cv2.imshow("", image)
cv2.waitKey(0)

    #    output_edge = cv2.Canny(output, 150, 400)
   #     output_edge = cv2.dilate(output_edge, kernel, iterations = 1)
    #    _, output_contours, _ = cv2.findContours(output_edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
 #       circleContour = []
#
 #       for c in output_contours:
  #          epsilon = 0.05 * cv2.arcLength(c, True)
   #         approx = cv2.approxPolyDP(c, epsilon, True)

    #        if len(approx) > 5:
     #           circleContour.append(approx)

      #  cv2.drawContours(img_cropped, circleContour, -1, (0, 0, 255), 1)
##