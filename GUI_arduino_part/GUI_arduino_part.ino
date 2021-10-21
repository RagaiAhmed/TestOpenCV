#include <Timer.h>

Timer myTimer ; 
#define redLed 4
#define blueLed 5
int mid;
String theQString;
int redtiming = 1000;
int bluetiming=1000;
bool blueToggle;
bool redToggle;
int idRed;
int idBlue;

void setup() {
  Serial.begin(9600);
  
 pinMode (redLed,OUTPUT);
 pinMode (blueLed,OUTPUT);

idRed = myTimer.every(redtiming,fnRed); 
idBlue = myTimer.every(bluetiming,fnBlue); 


}

void fnRed() {

  redToggle= digitalRead(redLed);
  redToggle=!redToggle;
  digitalWrite(redLed,redToggle);
 
}

void fnBlue() {
  blueToggle= digitalRead(blueLed);
  blueToggle=!blueToggle;
  digitalWrite(blueLed,blueToggle);
}


void loop() {

myTimer.update();

if (Serial.available()){

  myTimer.stop(idRed);
  myTimer.stop(idBlue);
  theQString=Serial.readString();
  if (theQString[0]=='R')
  { mid=theQString.indexOf('B');
  
    redtiming=theQString.substring(1,mid).toInt();
   idRed= myTimer.every(redtiming,fnRed); 
    
    bluetiming=theQString.substring(mid+1).toInt();
   idBlue= myTimer.every(bluetiming,fnBlue); 
    
    }
    else if (theQString[0]=='S')
    {
      digitalWrite(redLed,LOW);
      digitalWrite(blueLed,LOW);
      }
}

}
