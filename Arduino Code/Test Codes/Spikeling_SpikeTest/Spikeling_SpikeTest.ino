#include <analogWrite.h>

int Vm = 18;          // Red LED
int Spike = 19;       // Green & Blue LEDs + Buzzer

int Increment = 5;
int v;
int Delay = 0;
int bits = 1023;
int spike = bits - 5;

int BaudRate = 9600;

void setup() {
  Serial.begin(BaudRate);

  pinMode(Vm,OUTPUT);
  pinMode(Spike,OUTPUT);
  digitalWrite(Vm,LOW);
  digitalWrite(Spike,LOW);
  
  v = 0;
}

void loop() {
  analogWrite(Vm, v);
  v = v + Increment; 
    
  if(v >= spike){
    analogWrite(Spike, v);
  }  
  if(v < spike){
    analogWrite(Spike, 0);
  }

  if (v >= bits) {
    v = 0;
  }
  
  delay(Delay); // wait before next transition
  Serial.println(v);
}
