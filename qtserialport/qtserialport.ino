#define red_led 9
#define blue_led 10
void setup() {
  pinMode(red_led, OUTPUT);
  pinMode(blue_led, OUTPUT);

}

void loop() {
  if (Serial.available()){
    char led_specifier = Serial.read();
    int led_delay = Serial.parseInt();
    write_leds(led_specifier, led_delay);

}
void write_leds(char led, int blinking)
{
  if (led == 'S'){
    digitalWrite(red_led,LOW);
    digitalWrite(blue_led,LOW);
  }
  if (led == 'R'){
    digitalWrite(red_led,HIGH);
    delay(blinking);
    digitalWrite(red_led,LOW);
  }
  if (led == 'B'){
    digitalWrite(blue_led,HIGH);
    delay(blinking);
    digitalWrite(blue_led,LOW);
  }
