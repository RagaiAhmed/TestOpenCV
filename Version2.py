import cv2
import numpy as np
# First we read the image
img = cv2.imread("Examples/test3.png")
# Here we check if we've read the image right as if we don't the ode won't run
if img is not None:
    # Those are the counts of the shapes
    count_tri, count_squ, count_react, count_circle = 0, 0, 0, 0
    # Converting the image to GrayScale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Taking the threshold to convert it to binary image
    _, threshold = cv2.threshold(imgGray, 250, 255, cv2.THRESH_BINARY)
    # This copy will use it to draw the contours on it.
    imgContour = img.copy()
    # Now, we generate the contours from the threshold image
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    i = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        # here we are ignoring first counter because
        # findcontour function detects whole image as shape
        if i == 0:
            i = 1
            continue

        # cv2.approxPloyDP() function to approximate the shape
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)

        # using drawContours() function
        cv2.drawContours(imgContour, [contour], 0, (0, 0, 0), 1)
        # This function will generate the width and height to know if it's a rect or circle or square.
        x, y, w, h = cv2.boundingRect(approx)

        # incrementing shape count each contour
        # If it was 3 then the shape will be triangle.
        if len(approx) == 3:
            count_tri += 1
        # If it was 4 then the shape will be a small rectangle or a square.
        elif len(approx) == 4:
            if w < 300 and h < 300:
                aspRatio = w / float(h)
                if 0.94 < aspRatio < 1.3:
                    count_squ += 1
                else:
                    count_react += 1
        # And as we don't have hexagons or pentagons then more than 4 must be a circle
        else:
            if w < 300 and h < 300:
                count_circle += 1
    # This used to show the image after thresholding
    imgContour = cv2.resize(imgContour, (600, 400))
    cv2.imshow('img', imgContour)
    cv2.waitKey(0)
    print("Number of triangles =", count_tri
          , "\nNumber of Squares =", count_squ
          , "\nNumber of Rectangles =", count_react
          , "\nNumber of circles =", count_circle)
