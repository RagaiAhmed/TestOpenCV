#define RED_LED 7
#define BLUE_LED 8
void setup() {
  pinMode(RED_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);
  Serial.begin(9600);
}
 char r="";
void blink(int Rvalue,int Bvalue,char r)
{
  

    digitalWrite(RED_LED, HIGH);
    delay(Rvalue);
    digitalWrite(RED_LED, LOW);
    delay(Rvalue);
    digitalWrite(BLUE_LED, HIGH);
    delay(Bvalue);
    digitalWrite(BLUE_LED, LOW);
    delay(Bvalue);
  
}

int rValue;
int bValue;

void loop() {
  if (Serial.available()) {
     r = Serial.read();
    rValue = Serial.parseInt();
    char b = Serial.read();
    bValue = Serial.parseInt();
  }
    if(r=='R' || r=='B'){
      blink(rValue,bValue,r);
      
  }
  else{
    digitalWrite(BLUE_LED, LOW);
    digitalWrite(RED_LED, LOW);
  }


}
