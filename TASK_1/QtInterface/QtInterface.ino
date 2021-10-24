#define redLED 9
#define blueLED 10
String command, redDelay, blueDelay;
int i, j, red, blue;
int redState = LOW;
int blueState = LOW;
void setup() {
  Serial.begin(9600);
  pinMode(blueLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  digitalWrite(redLED, LOW);
  digitalWrite(blueLED, LOW);
}
void readCommand() {
  Serial.print("Enter the command :");
  while (!Serial.available());

  command = Serial.readString();
  Serial.println(command);
}
void blinkLED(int red, int blue) {
  long inMillis = millis();
  long prevMillis = millis();
  long prevMillis2 = millis();
  while (millis() - inMillis < 2000) {
    if (millis() - prevMillis >= red) {
      prevMillis = millis();
      if (redState == LOW)
        redState = HIGH;
      else
        redState = LOW;
    }
    if (millis() - prevMillis2 >= blue) {
      prevMillis2 = millis();
      if (blueState == LOW)
        blueState = HIGH;
      else
        blueState = LOW;
    }

    digitalWrite(blueLED, blueState);
    digitalWrite(redLED, redState);
  }
}
void loop() {
  redDelay.remove(0, redDelay.length());
  blueDelay.remove(0, blueDelay.length());
  readCommand();
  if (command != "S") {
    for (i = 1; command[i] != 'B'; i++) {
      redDelay += command[i];
    }
    for (j = i + 1; j < command.length(); j++) {
      blueDelay += command[j];
    }
    Serial.println(redDelay);
    Serial.println(blueDelay);
    red = redDelay.toInt();
    blue = blueDelay.toInt();
    blinkLED(red, blue);

  } else {
    digitalWrite(redLED, LOW);
    digitalWrite(blueLED, LOW);
  }
}