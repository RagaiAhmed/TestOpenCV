import cv2
import os

def extract_shapes(img):
    # resize the image
    #img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

    # converting image into grayscale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # setting threshold of gray image
    _, threshold = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)

    # using a findContours() function
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    i = 0

    # list for storing names of shapes
    for contour in contours:

        # here we are ignoring first counter because
        # findcontour function detects whole image as shape
        if i == 0:
            i = 1
            continue

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
            if len(approx) == 3:
                cv2.putText(img, 'Triangle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.9, (100, 100, 100), 2)

            elif len(approx) == 4:
                if w == h:
                    cv2.putText(img, 'Square', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.9, (100, 100, 100), 2)
                else:
                    cv2.putText(img, 'Rectangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (100, 100, 100), 2)
            else:
                cv2.putText(img, 'circle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.9, (100, 100, 100), 2)
    return img


path_to_images = os.getcwd()+'/Examples'
for img in os.listdir(path_to_images):
    image = cv2.imread(path_to_images+'/'+img)
    shapes = extract_shapes(image)
    cv2.imwrite(path_to_images+ '/' + img[0:-4] +'_shapes.png', shapes)

'''
img = cv2.imread('Examples/test1.png')
shapes = extract_shapes(img)
cv2.imshow('img',shapes)
cv2.waitKey(0)
cv2.destroyAllWindows()'''