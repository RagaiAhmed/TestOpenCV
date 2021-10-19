int redLed = 13;
int blueLed = 7;
unsigned long SpeedR,SpeedB;
unsigned long prevTimeRedled = millis();
unsigned long prevTimeBlueled = millis();
byte redLedState = LOW;
byte blueLedState = LOW;
String serialReading;

void setup() {
  pinMode(redLed,OUTPUT);
  pinMode(blueLed,OUTPUT);
  Serial.begin(9600);
  while (Serial.available() == 0) {}
  serialReading = Serial.readString();

}

void loop() {
    if(serialReading[0] == 'S'){
      digitalWrite(redLed, LOW);
      digitalWrite(blueLed, LOW);
    }
    else{
      int Separator = serialReading.indexOf('B');
      SpeedR = serialReading.substring(1,Separator).toInt();
      SpeedB = serialReading.substring(Separator+1).toInt();
      
      unsigned long timeNow = millis();
      if(timeNow - prevTimeRedled > SpeedR){
        prevTimeRedled += SpeedB;;
        if(redLedState == HIGH)
          redLedState = LOW;
        else
          redLedState = HIGH;
        digitalWrite(redLed, redLedState);    
      }
      
      if(timeNow - prevTimeBlueled > SpeedB){
        prevTimeBlueled += SpeedB;
        if(blueLedState == HIGH)
          blueLedState = LOW;
        else
          blueLedState = HIGH;
        digitalWrite(blueLed, blueLedState);    
      }
    }
  if (Serial.available())
    serialReading = Serial.readString();
}
