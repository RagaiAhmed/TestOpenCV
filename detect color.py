import cv2
import os
import numpy as np


def detect_color(img ,b ,g ,r):
    if r == 255 and b==0 and g ==0:
        color = 'RED'
    elif b == 255 and r ==0 and g ==0:
        color = 'BLUE'
    elif g == 255 and b ==0 and r == 0:
        color = 'GREEN'
    elif g == 242 and r== 255 and b == 0:
        color = 'Yellow'

    color_arr_to_be_detected = (img[:, :, 2] == r) & (img[:, :, 0] == b) & (img[:, :, 1] == g)
    color_arr_to_be_detected = color_arr_to_be_detected * 255
    color_arr_to_be_detected = color_arr_to_be_detected.astype(np.uint8)

    contours, _ = cv2.findContours(color_arr_to_be_detected, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # cv2.approxPloyDP() function to approximate the shape
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        x, y, w, h = cv2.boundingRect(contour)

        # using drawContours() function
        cv2.drawContours(img, [contour], 0, (0, 0, 0), 5)

        # finding center point of shape
        M = cv2.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10'] / M['m00']) - 20
            y = int(M['m01'] / M['m00']) + 20

        # putting shape name at center of each shape
        if w < 200 and h < 200:
            cv2.putText(img, color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (200, 50, 200), 2)


path_to_images = os.getcwd()+'/Examples/color detection'
for img in os.listdir(path_to_images):
    image = cv2.imread(path_to_images+'/'+img)

    detect_color(image, 0, 0, 255)
    detect_color(image, 255, 0, 0)
    detect_color(image, 0, 255, 0)
    detect_color(image, 0, 242, 255)

    cv2.imwrite(path_to_images+ '/' + img[0:-4] +'_detected_colors.png', image)