#define red_led 9
#define blue_led 10
void setup() {
  pinMode(red_led, OUTPUT);
  pinMode(blue_led, OUTPUT);
  int red_blinking_speed;
  int blue_blinking_speed;
  int previous_time_red = 0;
  int previous_time_blue = 0;

void setup() {

  pinMode(red_led, OUTPUT);
  pinMode(blue_led, OUTPUT);
  digitalWrite(red_led, LOW);
  digitalWrite(blue_led, LOW);

}

void loop() {

  int current_time = millis();
  char led_specifier;
  int led_blinking_speed;
  if (Serial.available()){
    char led_specifier = Serial.read();
    int led_blinking_speed = Serial.parseInt();
  }
  if (led_specifier == 'S'){
    digitalWrite(red_led,LOW);
    digitalWrite(blue_led,LOW);
  }
  else if (led_specifier == 'R'){
    red_blinking_speed = led_blinking_speed;
    if (current_time >= red_blinking_speed+previous_time_red){
      digitalWrite(red_led, !digitalRead(red_led));
      previous_time_red = current_time;
    }
  }
  
  else if (led_specifier == 'B'){
    blue_blinking_speed = led_blinking_speed;
    if (current_time >= blue_blinking_speed+previous_time_blue){
      digitalWrite(blue_led, !digitalRead(blue_led));
      previous_time_blue = current_time;
    }
  }
  
}
