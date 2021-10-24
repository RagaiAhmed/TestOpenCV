import numpy as np
import cv2

imagePath = input ("Please enter the required path : ")
img = cv2.imread(imagePath)

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

_, thrash = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


g_lower = np.array([36, 0, 0], dtype="uint8")
g_upper = np.array([70, 255,255], dtype="uint8")
g_mask = cv2.inRange(hsv,g_lower,g_upper)

y_lower = np.array([15,0,0], dtype="uint8")
y_upper = np.array([36, 255,255], dtype="uint8")
y_mask = cv2.inRange(hsv,y_lower,y_upper)

b_lower = np.array([100,150,0], dtype="uint8")
b_upper = np.array([120, 255, 255], dtype="uint8")
b_mask = cv2.inRange(hsv,b_lower,b_upper)


r_lower = np.array([0,80,80], dtype="uint8")
r_upper = np.array([20,255,255], dtype="uint8")
r_mask = cv2.inRange(hsv,r_lower,r_upper)


y_cnts = cv2.findContours(y_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
y_cnts = y_cnts[0] if len(y_cnts) == 2 else y_cnts[1]

g_cnts = cv2.findContours(g_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
g_cnts = g_cnts[0] if len(g_cnts) == 2 else g_cnts[1]

b_cnts = cv2.findContours(b_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
b_cnts = b_cnts[0] if len(b_cnts) == 2 else b_cnts[1]

r_cnts = cv2.findContours(r_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
r_cnts = r_cnts[0] if len(r_cnts) == 2 else r_cnts[1]

#COLOR DETECTION
for c in y_cnts:
    x,y,_,_ = cv2.boundingRect(c)
    cv2.putText(img,"Yellow",(x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

for c in g_cnts:
    x,y,_,_ = cv2.boundingRect(c)
    cv2.putText(img,"green",(x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

for c in b_cnts:
    x,y,_,_ = cv2.boundingRect(c)
    cv2.putText(img,"blue",(x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

for c in r_cnts:
    x,y,_,_ = cv2.boundingRect(c)
    cv2.putText(img,"red",(x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))


#SHAPE DETECTION
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 0)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 20
    
    if len(approx) == 3:
        cv2.putText(img,"Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        x1 ,y1, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
          cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
          cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        cv2.putText(img,"Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))


cv2.imshow("Shape Detector", img)
cv2.waitKey(0)
cv2.destroyAllWindows()