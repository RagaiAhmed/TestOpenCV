/*

*/

#define red_led 3
#define blue_led 4

char led;
int speed;

void setup() {
  
  pinMode(red_led,OUTPUT);
  pinMode(blue_led,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  
    if (Serial.available()) {
      
      led = Serial.read();
      speed = Serial.parseInt();    
    }
    
    if (led == 'R')
      blinkyBlinky(red_led,speed);
    else if (led == 'B')
      blinkyBlinky(blue_led,speed);
    else{ 
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
