

using namespace std;
int red_Led = 7;
int blue_Led = 8;
long rateR, rateB;
unsigned long previousTimeLed1 = millis();
unsigned long previousTimeLed2 = millis();
int red_Led1 = LOW;
int blue_Led1 = LOW;
String val;
void setup() {
  Serial.begin(9600);
  pinMode(red_Led, OUTPUT);
  pinMode(blue_Led, OUTPUT);
  while (Serial.available() == 0) {}
  val = Serial.readString();
}

void loop() {
  if (val.compareTo("S") == 0) {
    digitalWrite(blue_Led, LOW);
    digitalWrite(red_Led, LOW);
  }
  else {
    int bIndex = val.indexOf('B');
    rateR = val.substring(1, bIndex).toInt();
    rateB = val.substring(bIndex + 1).toInt();
    unsigned long currentTime = millis();
    if (currentTime - previousTimeLed1 > rateR) {
      previousTimeLed1 += rateR;
      if (red_Led1 == HIGH) {
        red_Led1 = LOW;
      }
      else {
        red_Led1 = HIGH;
      }
      digitalWrite(red_Led, red_Led1);
    }
    if (currentTime - previousTimeLed2 > rateB) {
      previousTimeLed2 += rateB;
      if (blue_Led1 == HIGH) {
        blue_Led1 = LOW;
      }
      else {
        blue_Led1 = HIGH;
      }
      digitalWrite(blue_Led, blue_Led1);
    }

  }
  if (Serial.available())
    val = Serial.readString();
}
