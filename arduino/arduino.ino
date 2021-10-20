#define red_led 9
#define blue_led 10

boolean red = false;
boolean blue = false;
boolean redStatue = true;
boolean blueStatue = true;

int red_speed;
int blue_speed;

int previousMillisRed;
int currentMillisRed;
int previousMillisBlue;
int currentMillisBlue;

void setup()
{
  pinMode(red_led, OUTPUT);
  pinMode(blue_led, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available()) {
    char led_specifier = Serial.read();
    int led_blink_speed = Serial.parseInt();
    control_leds(led_specifier, led_blink_speed);

    previousMillisRed = millis();
    previousMillisBlue = millis();
  }
  blinkk();
}

void control_leds(char led, int speedd)
{
  if (led == 'r') {
    red = true;
    red_speed = speedd;
  }


  if (led == 'b') {
    blue = true;
    blue_speed = speedd;
  }

  else if (led == 's') {
    red = false;
    blue = false;
    digitalWrite(red_led, LOW);
    digitalWrite(blue_led, LOW);
     redStatue = true;
     blueStatue = true;
  }


}

void blinkk() {
  if (red == true && blue == true) {

    digitalWrite(red_led, redStatue);
    currentMillisRed = millis();
    
    if (currentMillisRed - previousMillisRed >= red_speed) {
      previousMillisRed = currentMillisRed;
      redStatue = !redStatue;
    }

    digitalWrite(blue_led, blueStatue);
    currentMillisBlue = millis();
    
    if (currentMillisBlue - previousMillisBlue >= blue_speed) {
      previousMillisBlue = currentMillisBlue;
      blueStatue = !blueStatue;
    }

  }

}
