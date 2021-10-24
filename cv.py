import cv2 as cv
import numpy as np


# Detecting colors

# laod image
img = cv.imread('Examples/test3.png')
img = cv.resize(img, (600, 600), interpolation=cv.INTER_CUBIC)

# convert image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# convert image to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# configuring hsv for the colors in the image
red_lower = np.array([0, 70, 50], np.uint8)
red_upper = np.array([10, 255, 255], np.uint8)
red_mask = cv.inRange(hsv, red_lower, red_upper)

green_lower = np.array([50, 80, 100], np.uint8)
green_upper = np.array([102, 255, 255], np.uint8)
green_mask = cv.inRange(hsv, green_lower, green_upper)

blue_lower = np.array([110, 50, 50], np.uint8)
blue_upper = np.array([130, 255, 255], np.uint8)
blue_mask = cv.inRange(hsv, blue_lower, blue_upper)

yellow_lower = np.array([20, 100, 100], np.uint8)
yellow_upper = np.array([30, 255, 255], np.uint8)
yellow_mask = cv.inRange(hsv, yellow_lower, yellow_upper)

kernal = np.ones((5, 5), "uint8")

red_mask = cv.dilate(red_mask, kernal)
res_red = cv.bitwise_and(img, img, mask = red_mask)

green_mask = cv.dilate(green_mask, kernal)
res_green = cv.bitwise_and(img, img, mask = green_mask)

blue_mask = cv.dilate(blue_mask, kernal)
res_blue = cv.bitwise_and(img, img, mask = blue_mask)

yellow_mask = cv.dilate(yellow_mask, kernal)
res_yellow = cv.bitwise_and(img, img, mask = yellow_mask)

_, thresh = cv.threshold(gray, 250, 255, cv.CHAIN_APPROX_NONE)

# writing the color of the shape
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

red_contours, _ = cv.findContours(red_mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
green_contours, _ = cv.findContours(green_mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
blue_contours, _ = cv.findContours(blue_mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
yellow_contours, _ = cv.findContours(yellow_mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
for _, c in enumerate(red_contours):
    area = cv.contourArea(c)

    
    x, y, w, h = cv.boundingRect(c)
    cv.putText(img, "Red", (x, y), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 255))

for _, c in enumerate(green_contours):
    area = cv.contourArea(c)

    
    x, y, w, h = cv.boundingRect(c)
    cv.putText(img, "Green", (x, y), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0, 255, 0))

for _, c in enumerate(blue_contours):
    area = cv.contourArea(c)

    x, y, w, h = cv.boundingRect(c)
    cv.putText(img, "Blue", (x, y), cv.FONT_HERSHEY_TRIPLEX, 0.5, (255, 0, 0))

for _, c in enumerate(yellow_contours):
    area = cv.contourArea(c)

    x, y, w, h = cv.boundingRect(c)
    cv.putText(img, "Yellow", (x, y), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0, 255, 255))



# Detecting the shapes

# remove borders
for i in range(len(contours)-1, 0, -1):
    if contours[i].ravel()[1] == 0:
        contours.pop(i)
 
# count contours
for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
    cv.drawContours(img, [contour], 0, (0, 0, 0), 1)

    M = cv.moments(approx)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

    if len(approx) == 3:
        cv.putText(img, 'Triangle', (cx, cy), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 0), 1)

    elif len(approx) == 4:
        x, y, w, h = cv.boundingRect(approx)
        aspect_ratio = float(w) / h
        if aspect_ratio > 0.75 and aspect_ratio < 1.5:
            cv.putText(img, 'Square', (cx, cy), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 0), 1)
        else:
            cv.putText(img, 'Rectangle', (cx, cy), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 0), 1)

    elif len(approx) > 6:
        cv.putText(img, 'Circle', (cx, cy), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 0), 1)

cv.imshow('Shapes', img)

cv.waitKey(0)