#define RED_LED 7
#define BLUE_LED 8
void setup() {
  pinMode(RED_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);
  Serial.begin(9600);
}
void blinkRed(int Rvalue)
{
  while (true) {
    digitalWrite(RED_LED, HIGH);
    delay(Rvalue);
    digitalWrite(RED_LED, LOW);
    delay(Rvalue);
  }

}
void blinkBlue(int Bvalue)
{
  while (true) {
    digitalWrite(BLUE_LED, HIGH);
    delay(Bvalue);
    digitalWrite(BLUE_LED, LOW);
    delay(Bvalue);
  }

}
int rValue;
int bValue;
void loop() {
  if (Serial.available()) {
    char r = Serial.read();
    rValue = Serial.parseInt();
    char b = Serial.read();
    bValue = Serial.parseInt();
    if(r!='S'){
      blinkRed(rValue);
      blinkBlue(bValue);
  }
  else{
    digitalWrite(BLUE_LED, LOW);
    digitalWrite(RED_LED, LOW);
  }
}

}
