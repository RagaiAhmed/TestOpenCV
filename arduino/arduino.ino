/*

*/

#define red_led 3
#define blue_led 4

char led1 = ' ', led2 = ' ';
int speed1 = 0, speed2 = 0;

unsigned long long current_time_red = 0, current_time_blue = 0, previous_time_red = 0, previous_time_blue = 0;

void setup() {
  
  pinMode(red_led,OUTPUT);
  pinMode(blue_led,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  
    if (Serial.available()) {
      
      led1 = Serial.read();
      speed1 = Serial.parseInt();
      led2 = Serial.read();
      speed2 = Serial.parseInt();
    }
   
  
    if (led1 == 'R' && led2 == 'B')
    {
      Serial.print("true");
      current_time_red = millis();
      
      if (current_time_red - previous_time_red >= speed1){
        previous_time_red = current_time_red;
        digitalWrite(red_led,!digitalRead(red_led));
      }
      
      current_time_blue = millis();
      
      if (current_time_blue - previous_time_blue >= speed2){
        previous_time_blue = current_time_blue;
        digitalWrite(blue_led,!digitalRead(blue_led));
      }
    }
  
    else if (led1 == 'R' && led2 != 'B')
      blinkyBlinky(red_led,speed1);
  
    else if (led1 == 'B' && led2 != 'R')
      blinkyBlinky(blue_led,speed1);
      
    else if (led1 = 'S'){ 
      digitalWrite(red_led,LOW);
      digitalWrite(blue_led,LOW);
    }
}

void blinkyBlinky(int LED, int speed)
{
  
    digitalWrite(LED, HIGH);
    delay(speed);
    digitalWrite(LED, LOW);
    delay(speed);
  
}

