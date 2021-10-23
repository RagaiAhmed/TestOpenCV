import cv2

import numpy as np

from matplotlib import pyplot as plt
  

path = r'D:\opencv\test3.png'


# reading image

img1 = cv2.imread(path,1)
img = cv2.resize(img1, (800, 600)) 



# converting image into hsv image
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

  


red_lower = np.array([0, 200, 200])
red_upper = np.array([10, 255, 255])
red_mask = cv2.inRange(hsv, red_lower, red_upper)


green_lower = np.array([50, 100, 0])
green_upper = np.array([100, 255, 255])
green_mask = cv2.inRange(hsv, green_lower, green_upper)


blue_lower = np.array([94, 80, 2])
blue_upper = np.array([120, 255, 255])
blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)


yellow_lower = np.array([22, 93, 0])
yellow_upper = np.array([45, 255, 255])
yellow_mask = cv2.inRange(hsv,yellow_lower,yellow_upper)



# using a findContours() function
# yellow
contoursY, _ = cv2.findContours(
    yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#blue
contoursB, _ = cv2.findContours(
    blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# green
contoursG, _ = cv2.findContours(
    green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# red
contoursR, _ = cv2.findContours(
    red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
allContours = [contoursY,contoursB,contoursG,contoursR]


c=-1

# list for storing names of shapes
for contourArr in allContours:
    c=c+1
    
    for contour in contourArr:
    
        # here we are ignoring first counter because 
        # findcontour function detects whole image as shape
        if cv2.contourArea(contour) >= 15*1000:
        
            continue

    
        # cv2.approxPloyDP() function to approximate the shape
        approx = cv2.approxPolyDP(
            contour, 0.019 * cv2.arcLength(contour, True), True)
        

        # using drawContours() function
        cv2.drawContours(img, [contour], 0, (0, 0, 0), 1)
        
    




        # finding center point of shape using shape moment
        M = cv2.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])
    


        if len(approx) == 3:
            cv2.putText(img, 'Triangle', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
    
        elif len(approx) == 4:
            _,_,w,h = cv2.boundingRect(approx)
            r=float(w)/h
            if (r > 1.1 or r < 0.9):
                cv2.putText(img, 'rectangle', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
            else:
                cv2.putText(img, 'square', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

        elif len(approx) == 5:
            cv2.putText(img, 'Penta', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
    
        elif len(approx) == 6:
            cv2.putText(img, 'Hexa', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
    
        else:
            cv2.putText(img, 'circle', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
    

        y=y+30
        # putting shape colo at center of each shape
        if c==0:
            cv2.putText(img, 'Yellow', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
    
        elif c==1:
            cv2.putText(img, 'Blue', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
           
        elif c==2:
            cv2.putText(img, 'Green', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
    
        elif c==3:
            cv2.putText(img, 'Red', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
        




# displaying the image after drawing contours
cv2.imshow('shapes', img)
  
cv2.waitKey(0)
cv2.destroyAllWindows()