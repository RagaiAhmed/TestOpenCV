
# Test Open CV

**Go to documentation of :**
- [CV.py](#cv)
- [arduino.ino](#arduino)
- [Serial](#serial)

## [CV](CV.py)

The purpose of this code is to detect the shape and the color of each of the geometric shapes inside an image.

### Usage
- You need to install `OpenCV` and `NumPy` libraries
    - To install `OpenCV` write in your terminal `pip install opencv-python`
    - To install `NumPy` write in your terminal `pip install numpy`

### Issues
This code is not capable of detecting all colors or geometric shapes so you have to adjust it before usage to detect more shapes and colors 

---

## [Arduino](/arduino/arduino.ino)

The purpose of this code is to use `UART` communication protocole of arduino board to control the blinking of two leds.

### Usage
- You have to connect to the Arduino board using serial port
- To start blinking it is required to send a string with certain specifications
    - It must begins with uppercase letter `R`.
    - The letter must be followed with the amount of time in `milliseconds` needed for the first led to be turned on or off.
    - The number must be followed with uppercase letter `B`.
    - - The letter must be followed with the amount of time in `milliseconds` needed for the second led to be turned on or off
    - ***Example :*** 
        ```
        "R200B300"
        ```
        This means that the first led blink has a duration of `200 ms` (it is turned on for `200 ms` and off for another `200 ms`) and the other led blink has a duration of `300 ms` (it is turned on for `300 ms` and off for another `300 ms`).
- To stop blinking you have to send uppercase letter `S`.

---

## [Serial](/Serial)

The purpose of this code is to use `UART` communication protocole between a Computer device and an Arduino Uno board to control the blinking of two leds (for arduino code go to [arduino.ino](/arduino/arduino.ino)).

### Usage
- You have to connect to the Arduino board using serial port and the GUI will pick it automatically
- There are two `edit line` fields, the first one for the duration of the first led and the second one is for the second led.
- Enter the duration of each led in its `edit line` field in `milliseconds`.
- To **start** blinking click on the `on` button after writing numbers in the two `edit line` fields.
- To **stop** blinking click on the `off` button.
