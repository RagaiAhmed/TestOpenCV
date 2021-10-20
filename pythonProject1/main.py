import cv2
import numpy as np

# reading image
img = cv2.imread('test1.png')

# converting image into hsv image
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Defining lower and upper bound HSV values
lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])

lower_red = np.array([-10, 100, 100])
upper_red = np.array([10, 255, 255])

lower_blue = np.array([110, 100, 100])
upper_blue = np.array([130, 255, 255])

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([40, 255, 255])

# Defining mask for detecting color
mask1 = cv2.inRange(hsv, lower_green, upper_green)
resultGreen = cv2.bitwise_and(img, img, mask=mask1)
_, thresholdGreen = cv2.threshold(mask1, 250, 255, cv2.THRESH_BINARY)
cntGreen,_ = cv2.findContours(thresholdGreen, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cntg in cntGreen:
    Mgreen = cv2.moments(cntg)
    if Mgreen['m00'] != 0.0:
        x = int(Mgreen['m10'] / Mgreen['m00'])
        y = int(Mgreen['m01']/ Mgreen['m00'])
        cv2.putText(img, 'Green', (x, y+20), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 0), 2)

mask2 = cv2.inRange(hsv, lower_blue, upper_blue)
resultBlue = cv2.bitwise_and(img, img, mask=mask2)
_, thresholdBlue = cv2.threshold(mask2, 250, 255, cv2.THRESH_BINARY)
cntBlue,_ = cv2.findContours(thresholdBlue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cntb in cntBlue:
    Mblue = cv2.moments(cntb)
    if Mblue['m00'] != 0.0:
        x = int(Mblue['m10'] / Mblue['m00'])
        y = int(Mblue['m01']/ Mblue['m00'])
        cv2.putText(img, 'Blue', (x, y+20), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 0), 2)

mask3 = cv2.inRange(hsv, lower_red, upper_red)
resultRed = cv2.bitwise_and(img, img, mask=mask3)
_, thresholdRed = cv2.threshold(mask3, 250, 255, cv2.THRESH_BINARY)
cntRed,_ = cv2.findContours(thresholdRed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cntr in cntRed:
    Mred = cv2.moments(cntr)
    if Mred['m00'] != 0.0:
        x = int(Mred['m10'] / Mred['m00'])
        y = int(Mred['m01'] / Mred['m00'])
        cv2.putText(img, 'Red', (x, y+20), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 0), 2)

mask4 = cv2.inRange(hsv, lower_yellow, upper_yellow)
resultYellow = cv2.bitwise_and(img, img, mask=mask4)
_, thresholdYellow = cv2.threshold(mask4, 250, 255, cv2.THRESH_BINARY)
cntYellow,_ = cv2.findContours(thresholdYellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnty in cntYellow:
    MYellow = cv2.moments(cnty)
    if MYellow['m00'] != 0.0:
        x = int(MYellow['m10'] / MYellow['m00'])
        y = int(MYellow['m01'] / MYellow['m00'])
        cv2.putText(img, 'Yellow', (x, y+20), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 0), 2)

# setting threshold of hsv image
_, threshold = cv2.threshold(mask1+mask2+mask3+mask4, 250, 255, cv2.THRESH_BINARY)

# using a findContours() function
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0
# list for storing names of shapes
for contour in contours:

    # here we are ignoring first counter because find contour function detects whole image as shape
    if i == 0:
        i = 1
        continue

    # cv2.approxPloyDP() function to approximate the shape
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

    # using drawContours() function
    cv2.drawContours(img, [contour], 0, (0, 0, 0), 3)

    # finding center point of shape
    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])
        # putting shape color

        # putting shape name at center of each shape
        if len(approx) == 3:
            cv2.putText(img, 'Triangle', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 0), 2)

        elif len(approx) == 4:
            x1, y1, w, h = cv2.boundingRect(approx)
            aspectRatio = float(w) / h
            if (aspectRatio >= 0.95) and (aspectRatio <= 1.05):
                cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
            else:
                cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)

        else:
            cv2.putText(img, 'Circle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

# displaying the image after drawing contours
cv2.imshow('Detected shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()