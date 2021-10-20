#define red_led 9
#define blue_led 10

char recieved;
int red_blink;
int blue_blink;
int led_red_interval;
int led_blue_interval;
int previous_time_red = 0;
int previous_time_blue = 0;
void setup()
{
  pinMode(red_led, OUTPUT);
  pinMode(blue_led, OUTPUT);
  digitalWrite(red_led, LOW);
  digitalWrite(blue_led, LOW);
  Serial.begin(9600);
}

void loop()
{
  int current_time = millis(), led_interval;
  if (Serial.available()){
    recieved = Serial.read();
    led_interval = Serial.parseInt();
}
if (recieved == 's'){
  digitalWrite(red_led, LOW);
  digitalWrite(blue_led, LOW);
}
else{
   if (recieved=='R'){
    led_red_interval = led_interval;
}
if (current_time >= previous_time_red+led_red_interval){
      digitalWrite(red_led, !digitalRead(red_led));
      previous_time_red = current_time;
    } 
 if (recieved=='B'){
    led_blue_interval = led_interval;
}
if (current_time >= previous_time_blue+led_blue_interval){
      digitalWrite(blue_led, !digitalRead(blue_led));
      previous_time_blue = current_time;
    }  
}

}
