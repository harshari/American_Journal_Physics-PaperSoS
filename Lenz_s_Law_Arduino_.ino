#define pin1 A6
#define pin2 8
#define pin3 3
#define led_vcc 12
#define led_gnd 10

long int t1;
long int t2;
void setup() {
  Serial.begin(115200); 
  //Serial.begin(115200); 
  pinMode(pin1,INPUT);
  pinMode(pin2,INPUT);
  pinMode(pin3,INPUT);
  pinMode(led_vcc,OUTPUT);
  pinMode(led_gnd,OUTPUT);
  digitalWrite(led_vcc,HIGH);
  digitalWrite(led_gnd,LOW);
}
 
void loop() {
  while(true){
    //When using hall effect sensor in pullup, change digitalRead(pin2) == LOW 
    //when using standard reed switch, change it to digitalRead(pin2) == HIGH
  if(digitalRead(pin2)==HIGH){
    t1=millis();
    break;
  }}

  
  while(true){
    if(digitalRead(pin3)==HIGH)
      {
        for(int i=0;i<30;i++)
          Serial.println(analogRead(pin1));
        Serial.println("3000");
        Serial.println(t1);
        Serial.println(millis());
        break;    
      }
      else
      {
        Serial.println(analogRead(pin1));
      }
}
delay(5000);
}
//New addition Downward changed on 17 March

/*
 while(true){
  if(digitalRead(pin2)==HIGH){
    t2=millis();
    break; 
  }}
  while(true){
    if(digitalRead(pin3)==HIGH)
      {
        for(int i=0;i<30;i++)
          Serial.println(analogRead(pin1));
        Serial.println("3000");
        Serial.println(t2);
        Serial.println(millis());
        break;    
      }
      else
      {
        Serial.println(analogRead(pin1));
      }
}
}

*/
