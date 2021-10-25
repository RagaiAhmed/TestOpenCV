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
# QT code
the code consists of two main parts the GUI part and the Dialoge code part.
## GUI
The gui contains:
  1. two push buttons (on, off)
  2. two line text
  3. close button 
## dialoge.cpp
* we include <QSerialPort>,<QSerialPortInfo> libraries to be able to communicate with the arduino using the serial port.
* we create object form the QSerialPort called arduino.
* we loops on the available serial ports to check if any of the ports matches the arduino's vendor and product id.
  if there is a match we assign 'true' to a variable called  arduino_is_available and store the name of this serial port in a variable called arduino_port_name.
* if arduino_is_available is true we start seting the serial port by using several function:
  1. setPortName() which set the portName to the arduino_port_name(variable we got in the last loop)
  2. open() which take the mode of the serial which is 'WriteOnly' in our case as we just need to write in the serial port .
  3. setBaudRate() which takes the baudRate as a paramerter which is 9600 in our case (same as in the arduino's code) .
  4. setDataBits() which takes the number of date bits will be sent which is 'DATA8' in our case which is the prefered value.
  5. setParity() which determines the parity bit which is NOParity in our case.
  6. setStopBits()  which determines the stop bits 1 or 2 which is OneStop in our case.
  7. setFlowControl() which determines the method in which a serial device controls the amount of data being transmitted to itself which is NoFlowControl in our case.
#### on_pushButton_clicked function
this function works when the ON button is pressed.
it store the text in both lineEdit 1 and 2 in two variables called red and blue  in a result varible
then it concatinate them in a "R+red+B+blue" formate 
then it call the function sendMESSAGE() which takes the result.
#### on_pushButton_2_clicked function
this function works when the Off button is pressed.
it call sendMESSAGE() function which takes "S" as a parameter.
#### sendMESSAGE(result) function
this function checks if the arduino is Writable and write the result on it after converting it fron Qstring to stdString.
# Arduino Code
* this code we define REd and Blue led to 7, 8 pins as an output
* it has a function called blink which take the RValue, BValue which comes form the serialport, it also takes r (which is the fisrt letter sent by the serial)
### loop function
* it checks if the serial is availble to be read, then it reads r and rValue and b and Bvlue from the reseved format (R red B blue)
* if(r==R or r==B) it call blink function
* if its 'S' or any thing else it turn both led off.




 