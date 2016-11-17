int analog_pin = 0;
void setup() {
Serial.begin(9600);
pinMode(2,OUTPUT);
pinMode(3,OUTPUT);
pinMode(4,OUTPUT);
pinMode(5,OUTPUT);
pinMode(6,OUTPUT);
}

void loop() {
  int val = analogRead(analog_pin);
  //Serial.println(val);
  digitalWrite(2,LOW);
  digitalWrite(3,LOW);
  digitalWrite(4,LOW);
  digitalWrite(5,LOW);
  digitalWrite(6,LOW);
unsigned char c = (unsigned char )(((float)analogRead(0)/850.0)*255.0);
Serial.println((unsigned int)c);
if (c > 50){
  digitalWrite(2,HIGH);
  if (c>100){
    digitalWrite(3,HIGH);
    if (c>150){
      digitalWrite(4,HIGH);
      if (c>200){
        digitalWrite(5,HIGH);
        if (c>230){
          digitalWrite(6,HIGH);
        }
      }

    }
    
  }
}
delay(250);



  
}
