import cv2
import numpy as np
import matplotlib.pyplot as plt

image_name = input()

font = cv2.FONT_HERSHEY_COMPLEX
img1 = cv2.imread(image_name)
img = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
image_RGB = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
image_hsv = cv2.cvtColor(image_RGB, cv2.COLOR_RGB2HSV)

_, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, 0, 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 3:
        cv2.putText(img1, "Triangle", (x, y), font, 1, 0)
    elif len(approx) == 4:
        cv2.putText(img1, "Rectangle", (x, y), font, 1, 0)
    elif len(approx) == 5:
        cv2.putText(img1, "Pentagon", (x, y), font, 1, 0)
    elif 6 < len(approx) < 15:
        cv2.putText(img1, "Ellipse", (x, y), font, 1, 0)
    else:
        cv2.putText(img1, "Circle", (x, y), font, 1, 0)


lower_red = np.array([0, 150, 50])
upper_red = np.array([10, 255, 255])

lower_green = np.array([45, 150, 50])
upper_green = np.array([65, 255, 255])

lower_yellow = np.array([25, 150, 50])
upper_yellow = np.array([35, 255, 255])

lower_light_blue = np.array([95, 150, 0])
upper_light_blue = np.array([110, 255, 255])

lower_cyan = np.array([85, 150, 0])
upper_cyan = np.array([95, 255, 255])

lower_dark_blue = np.array([115, 150, 0])
upper_dark_blue = np.array([125, 255, 255])


mask_green = cv2.inRange(image_hsv, lower_green, upper_green)
mask_yellow = cv2.inRange(image_hsv, lower_yellow, upper_yellow)
mask_light_blue = cv2.inRange(image_hsv, lower_light_blue, upper_light_blue)
mask_cyan = cv2.inRange(image_hsv, lower_cyan, upper_cyan)
mask_dark_blue = cv2.inRange(image_hsv, lower_dark_blue, upper_dark_blue)
mask_red = cv2.inRange(image_hsv,lower_red,upper_red)

mask = mask_cyan + mask_dark_blue + mask_red\
       + mask_light_blue + mask_green

result = cv2.bitwise_and(image_RGB, image_RGB, mask = mask)
cv2.imshow("result", result)
cv2.imshow("shapes", img1)
cv2.waitKey(-1)
cv2.destroyAllWindows()
