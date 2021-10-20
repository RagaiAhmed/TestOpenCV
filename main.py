import cv2
import numpy as np

i = 0
img = cv2.imread('test3.png')
scale_percent = 60
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

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
masks = [mask1, mask2, mask3, mask4, mask5]
color = ["Red", "Blue", "green", "yellow", "grey"]
for mask in masks:
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        cv2.drawContours(img, [approx], 0, 0, 3)
        x = approx.ravel()[0] + 5
        y = approx.ravel()[1] - 5
        cv2.putText(img, color[i], (x, y+50), cv2.FONT_HERSHEY_COMPLEX, 0.5, 0)

        if len(approx) == 3:
            cv2.putText(img, "Triangle", (x, y+25), cv2.FONT_HERSHEY_COMPLEX, 0.5, 0)
        elif len(approx) == 4 or 6:
            x1, y1, w, h = cv2.boundingRect(approx)
            aspectRatio = float(w) / h
            if 0.95 <= aspectRatio <= 1.05:
                cv2.putText(img, "Square", (x, y+25), cv2.FONT_HERSHEY_COMPLEX, 0.5, 0)
            else:
                cv2.putText(img, "Rectangle", (x, y+25), cv2.FONT_HERSHEY_COMPLEX, 0.5, 0)
        else:
            cv2.putText(img, "Circle", (x, y+25), cv2.FONT_HERSHEY_COMPLEX, 0.5, 0)
    i = i + 1

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
