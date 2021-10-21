#define red 13
#define blue 12

String message;
int red_time;
int blue_time;
int r = 0, b = 0;

long timer;
long r_timer;
long b_timer;

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
      r_timer = 0;
      b_timer = 0;
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
      
      r_timer = millis();
      Serial.println(r_timer);
      b_timer = millis();
    }
    
  }
  if((red_time > 0) && (blue_time > 0))
  {
    if ((timer - r_timer >= red_time) && red_time > 0){
    r_timer = millis();
    Serial.print("timer: ");
    Serial.println(r_timer);
    Serial.print("\ttime: ");
    Serial.println(red_time);
    
    digitalWrite(red, !(digitalRead(red)));
  }

  if ((timer - b_timer >= blue_time) && blue_time > 0){
    b_timer = millis();
    Serial.print("timer: ");
    Serial.println(b_timer);
    Serial.print("\ttime: ");
    Serial.println(blue_time);
    
    digitalWrite(blue, !(digitalRead(blue)));
  }
  }
  else
  {
    digitalWrite(red, LOW);
    digitalWrite(blue, LOW);
  }
  timer = millis();
}
