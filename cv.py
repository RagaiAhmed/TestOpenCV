import cv2 as cv

img = cv.imread('Examples/test3.png')
img = cv.resize(img, (600, 600), interpolation=cv.INTER_CUBIC)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(gray, 250, 255, cv.CHAIN_APPROX_NONE)

contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

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
        cv.putText(img, 'Triangle', (cx, cy), cv.FONT_HERSHEY_TRIPLEX, 0.5, (255, 0, 255), 1)

    elif len(approx) == 4:
        x, y, w, h = cv.boundingRect(approx)
        aspect_ratio = float(w) / h
        print(x, ' ', y, ' ', aspect_ratio)
        if aspect_ratio > 0.75 and aspect_ratio < 1.5:
            cv.putText(img, 'Square', (cx, cy), cv.FONT_HERSHEY_TRIPLEX, 0.5, (255, 0, 255), 1)
        else:
            cv.putText(img, 'Rectangle', (cx, cy), cv.FONT_HERSHEY_TRIPLEX, 0.5, (255, 0, 255), 1)

    elif len(approx) > 6:
        print(len(approx))
        cv.putText(img, 'Circle', (cx, cy), cv.FONT_HERSHEY_TRIPLEX, 0.5, (255, 0, 255), 1)

cv.imshow('Shapes', img)

cv.waitKey(0)