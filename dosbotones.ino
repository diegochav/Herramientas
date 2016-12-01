int dato =0;
int dato2 =0;
void setup(){
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  pinMode(12,OUTPUT);
}
void loop(){
  if(Serial.available() >0){
    dato = Serial.read();
    
    //Serial.write(dato);

    if(dato == 'a'){
      digitalWrite(13,HIGH);
    }

    else if(dato =='z'){
      digitalWrite(13,LOW);
    }
    
    if(dato=='b'){
      digitalWrite(12,HIGH);
      
      }

     else if(dato=='x'){
      digitalWrite(12,LOW);
      }
  }
}

