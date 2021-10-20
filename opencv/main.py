import cv2
import numpy as np

image = cv2.imread('test1.png')
img = cv2.resize(image, (960, 800))
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])
mask2 = cv2.inRange(hsv, lower_blue, upper_blue)

lower_green = np.array([36, 25, 25])
upper_green = np.array([70, 255, 255])
mask3 = cv2.inRange(hsv, lower_green, upper_green)

lower_yellow = np.array([22, 93, 0])
upper_yellow = np.array([45, 255, 255])
mask4 = cv2.inRange(hsv, lower_yellow, upper_yellow)

lower_grey = np.array([0, 0, 0])
upper_grey = np.array([350, 55, 100])
mask5 = cv2.inRange(hsv, lower_grey, upper_grey)

Red_contours, _ = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for cont1 in Red_contours:
    approx = cv2.approxPolyDP(cont1, 0.01 * cv2.arcLength(cont1, True), True)
    x = approx.ravel()[0]+5
    y = approx.ravel()[1]-20
    cv2.putText(img, "Red", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, 0)

Blue_contours, _ = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for cont2 in Blue_contours:
    approx = cv2.approxPolyDP(cont2, 0.01 * cv2.arcLength(cont2, True), True)
    x = approx.ravel()[0]+5
    y = approx.ravel()[1]-20
    cv2.putText(img, "Blue", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, 0)

Green_contours, _ = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for cont3 in Green_contours:
    approx = cv2.approxPolyDP(cont3, 0.01 * cv2.arcLength(cont3, True), True)
    x = approx.ravel()[0]+5
    y = approx.ravel()[1]-20
    cv2.putText(img, "Green", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, 0)

Yellow_contours, _ = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for cont4 in Yellow_contours:
    approx = cv2.approxPolyDP(cont4, 0.01 * cv2.arcLength(cont4, True), True)
    x = approx.ravel()[0]+5
    y = approx.ravel()[1]-20
    cv2.putText(img, "Yellow", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, 0)

Grey_contours, _ = cv2.findContours(mask5, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for cont5 in Grey_contours:
    approx = cv2.approxPolyDP(cont5, 0.01 * cv2.arcLength(cont5, True), True)
    x = approx.ravel()[0]+5
    y = approx.ravel()[1]-5
    cv2.putText(img, "Grey", (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 0.5, 0)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    #cv2.drawContours(img, [approx], 0, 0, 3)
    x = approx.ravel()[0] + 5
    y = approx.ravel()[1] - 5
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, 0)
    elif len(approx) == 4:
        x1, y1, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w) / h
        if 0.95 <= aspectRatio <= 1.05:
            cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, 0)
        else:
            cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, 0)
    else:
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, 0)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()