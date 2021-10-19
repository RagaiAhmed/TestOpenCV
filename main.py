import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('test2.png')
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converting the img to gray
    _, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # converting the img to HSV

    lower_red = np.array([0, 150, 50], np.uint8)    # the lower and higher for each color
    upper_red = np.array([10, 255, 255], np.uint8)
    lower_green = np.array([45, 150, 50], np.uint8)
    upper_green = np.array([65, 255, 255], np.uint8)
    lower_yellow = np.array([25, 150, 50], np.uint8)
    upper_yellow = np.array([35, 255, 255], np.uint8)
    lower_blue = np.array([115, 150, 0], np.uint8)
    upper_blue = np.array([125, 255, 255], np.uint8)
    # creating masks for each color with respect to its lower and higher ends
    red_mask = cv2.inRange(imgHSV, lower_red, upper_red)
    green_mask = cv2.inRange(imgHSV, lower_green, upper_green)
    yellow_mask = cv2.inRange(imgHSV, lower_yellow, upper_yellow)
    blue_mask = cv2.inRange(imgHSV, lower_blue, upper_blue)

    kernal = np.ones((5, 5), "uint8")
    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(img, img, mask=red_mask)
    green_mask = cv2.dilate(green_mask, kernal)
    res_green = cv2.bitwise_and(img, img, mask=green_mask)
    yellow_mask = cv2.dilate(yellow_mask, kernal)
    res_yellow = cv2.bitwise_and(img, img, mask=yellow_mask)
    blue_mask = cv2.dilate(blue_mask, kernal)
    res_blue = cv2.bitwise_and(img, img, mask=blue_mask)

    contours1, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)   # Creating contour for the red color
    for contour in contours1:
        x1, y1, w1, h1 = cv2.boundingRect(contour)
        cv2.putText(img, "red ", (x1 - 20, y1), cv2.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 0))

    contours2, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Creating contour for the green color
    for contour in contours2:
        x2, y2, w2, h2 = cv2.boundingRect(contour)
        cv2.putText(img, "green ", (x2 - 40, y2), cv2.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 0))

    contours3, _ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Creating contour for the blue color
    for contour in contours3:
        x3, y3, w3, h3 = cv2.boundingRect(contour)
        cv2.putText(img, "blue", (x3 - 40, y3 + 20), cv2.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 0))

    contours4, _ = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Creating contour for the yellow color
    for contour in contours4:
        x4, y4, w4, h4 = cv2.boundingRect(contour)
        cv2.putText(img, "yellow", (x4 - 50, y4 + 20), cv2.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 0))

    contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)   # Creating contours for shapes
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        cv2.drawContours(img, [approx], 0, (50, 50, 150), 5)
        x = approx.ravel()[0] - 4
        y = approx.ravel()[1] - 4
        if len(approx) == 3:   # if the approx = 3 it means that its triangle
            cv2.putText(img, "TRIANGLE", (x, y), cv2.FONT_HERSHEY_COMPLEX, .6, (220, 0, 0))
        elif len(approx) == 4:  # if the approx = 4 it means that its square or rectangle
            _, _, w, h = cv2.boundingRect(approx)
            ratio = w / h
            if 0.95 <= ratio <= 1.05:  # if the ratio bet the width height is approximately 1 so that its square
                cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (220, 0, 0))
            else:
                cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (220, 0, 0))
        else:
            cv2.putText(img, "CIRCLE", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (220, 0, 0))

    cv2.imshow("shapes", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
