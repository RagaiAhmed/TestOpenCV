# MIA Task1

>Robotics Team in Faculty of Engineering, Alexandria University.

---

### Table of Contents
- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

---

## Description
There are two main functions of this project:
- First is working on some
images to detect the shapes and colors of objects in images.
- Second is build a gui using qt5 with c++, and establish a communication
between the GUI and an Arduino board
#### Packages used

- opencv
- numpy
- qt5

---

## How To Use
#### For Part One (Shape & Color Detection):
- 'Examples' folder have two folders one for shape detection and another for color detection.
- when the cv.py script is run it will loop over 3 images in the 'Examples/shape detection'
and outputs 3 shape detected images.
- when the 'detect color.py' script is run it will loop over 3 images in the 'Examples/color detection'
and outputs 3 color detected images.

#### For Part Two (GUI & Arduino):
- 'Task1GUI' folder is a qt5 project file, it can be opened in the qt creator
and run from there. When running the GUI App will appear with two input fields
and two buttons. 
- The two input fields take led's blink speed in us.
- If ON is pressed then, the two leds will blink each with its entered speed.
- If OFF is pressed then, the two leds will turn off.
- 'arduino' folder has the arduino script. Note that the two leds need
to be connected to pins 9,10.
- The communication between the Arduino and GUI is vis serial at baud rate 9600.
- The GUI will automatically figure out which port the arduino board is connected to
and establish the serial communication.

[Back To The Top](#MIA Task1)

---

## References
- numpy - [numpy.org](https://numpy.org/doc/1.21/user/index.html)
- opencv - [opencv.org](https://docs.opencv.org/4.5.4/)

---

## License

---

## Author Info

- Twitter - [@eslamdyab21](https://twitter.com/EslamDyab10)
- Email - [@Eslam Dyab](es-eslam.dyab2019@alexu.edu.eg)

[Back To The Top](#MIA Task1)

