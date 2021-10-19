import numpy as np
import cv2 as cv
import imutils

img = cv.imread('Examples/test1.png')

#-- we scale the test image so it fits in the screen
new_height = int(img.shape[0] * 0.75)
new_width = int(img.shape[1] * 0.75)
dimensions = (new_width, new_height)
img = cv.resize(img, dimensions, interpolation=cv.INTER_AREA)
#cv.imshow('TEST 1', img)

#-- we transform the image to a grayscale version:
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#-- we get hsv version
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow("hsv", hsv)

#two methods to find contours: canny edges and threshold,
#this is the threshold method:
ret, thresh = cv.threshold(imgGray, 230, 255, cv.THRESH_BINARY)
#cv.imshow('Thresh', thresh)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'Number of contours is {len(contours)}')

imgGray = cv.drawContours(thresh, contours, -1, (0,0,255), 1)
#cv.imshow('Contours Drawn', imgGray)

# for loop to detect shapes
for contour in contours:
    approx = cv.approxPolyDP(contour, 0.015 * cv.arcLength(contour, True), True)
    #cv.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    if len(approx) == 3:
        cv.putText(img, "Triangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        x1, y1, w, h = cv.boundingRect(approx)
        aspectRatio = float(w) / h
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv.putText(img, "Square", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv.putText(img, "Rectangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        cv.putText(img, "Circle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

#determining color
#Red Color
lower_red = np.array([0,100,100])
upper_red = np.array([7,255,255])

# yellow color
lower_yellow = np.array([25,100,100])
upper_yellow = np.array([30,255,255])

#green color
lower_green = np.array([40,70,80])
upper_green = np.array([70,255,255])

#blue color
lower_blue = np.array([90,60,0])
upper_blue = np.array([121,255,255])

yellow = cv.inRange(hsv, lower_yellow, upper_yellow)
green = cv.inRange(hsv, lower_green, upper_green)
blue = cv.inRange(hsv, lower_blue, upper_blue)
red = cv.inRange(hsv, lower_red, upper_red)

contours_red = cv.findContours(red,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
contours_red = imutils.grab_contours(contours_red)

contours_yellow = cv.findContours(yellow,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
contours_yellow = imutils.grab_contours(contours_yellow)
#
contours_blue = cv.findContours(blue,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
contours_blue = imutils.grab_contours(contours_blue)
#
contours_green = cv.findContours(green,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
contours_green = imutils.grab_contours(contours_green)

#for loops for each color
for contour in contours_red:
    M = cv.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0
    cv.putText(img, "red", (cX - 20, cY - 20), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

for contour in contours_yellow:
    M = cv.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0
    cv.putText(img, "yellow", (cX - 20, cY - 20), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

for contour in contours_blue:
    M = cv.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0
    cv.putText(img, "blue", (cX - 20, cY - 20), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

for contour in contours_green:
    M = cv.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0
    cv.putText(img, "green", (cX - 20, cY - 20), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

cv.imshow("FINAL", img)
cv.waitKey(0)
