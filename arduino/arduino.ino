#define red 13
#define blue 12

String message;
int red_time;
int blue_time;
int r = 0, b = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(red, OUTPUT);
  pinMode(blue, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0)
  {
    message = Serial.readString();
    
    if(message == "S")
    {
      digitalWrite(red, LOW);
      digitalWrite(blue, LOW);
    }
    else
    {
      
      for(int i = 0; i < message.length(); i++)
      {
        if(message[i] == 'R')
        {
          r = i;
        }
        if(message[i] == 'B')
        {
          b = i;
        }
      }
      red_time = message.substring(r+1, b).toInt();
      blue_time = message.substring(b + 1, message.length()).toInt();
      Serial.println(red_time);
      Serial.println(blue_time);
      digitalWrite(blue, HIGH);
      digitalWrite(red, HIGH);
      
      delay(red_time);
      digitalWrite(red, LOW);
      delay(blue_time);
      digitalWrite(blue, LOW);
    }
    
  }
}
