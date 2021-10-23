# OpenCV
In the first part of the code we load the picture using imread function then we convert it to gray mode and HSV mode and save both of this modes into new pictures imgGrey , imgHSV.
* imgGrey is used for shape detection.
* imgHSV is used for color detectionn.
## color detection
* we define the lower end and upper end for each color using np arrays of the Hue, Saturation and Value of the color.
* we define new pictures in range of the color ends to merge it with the original picture.
* we get the contours of each color using findContours function. after getingthe contours for the color we loop on it and put the name of the color on it.
## shape detection
* we apply Image Thresholding to the imgGrey using threshold function on the mode of COLOR_BGR2GRAY which returns two values one of them is thrash.
* we get the contours of the shapes using findContours function which take three parameters the photo which is the  thrash and the mode which is RETR_TREE and the method which is CHAIN_APPROX_NONE
* we loop over these contours, inside the loop we use approxPolyDP function which provides an approximation of a shape of a contour and takes the curve and epsilon (Parameter specifying the approximation accuracy) and closed(If true, the approximated curve is closed) as a parameters
* we draw the contours the we get the x, y coordinates useing approx.ravel() function.
* then we check the lenth of  the approx 
  1. if its 3 then its triangle
  2. if its 4 we have two options square or rectangle so we use boundingRect method which will take this approx as a parameter and return the wedth and hight
     if the ratio bet the width height is approximately 1 so that its square else its rectangle.
  3. else, its a circle.
  