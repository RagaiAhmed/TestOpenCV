#define red_led 9
#define blue_led 10

boolean red = false;
boolean blue = false;

int red_speed;
int blue_speed;

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
    //Serial.println(led_specifier);
    //Serial.println(led_blink_speed);
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
  }


}

void blinkk() {
  if (red == true) {
    digitalWrite(red_led, HIGH);
    delay(red_speed);
    digitalWrite(red_led, LOW);
    delay(red_speed);
  }

  if (blue == true) {
    digitalWrite(blue_led, HIGH);
    delay(blue_speed);
    digitalWrite(blue_led, LOW);
    delay(blue_speed);
  }
}
