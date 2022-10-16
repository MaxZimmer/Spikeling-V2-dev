#include <analogWrite.h>
#include "Izhikevich_parameters.h"
#include "Settings.h"
#include "Mode_LEDS.h"


float v; // voltage in Iziekevich model
float u; // recovery variable in Iziekevich model


int Vm_min = -90;
int Vm_max = 20;
int Vm_spike = -30;
int Vm_peak = 30;
boolean spike = false;
int I_Stim = 0;
int spike_count = 0;
int Stim_state;

int Mode = 0;

long previous_time = 0;
unsigned long current_time;

void setup() {
  Serial.begin(BaudRate);

  pinMode(pinVm,OUTPUT);
  pinMode(pinSpike,OUTPUT);
  digitalWrite(pinVm,LOW);
  digitalWrite(pinSpike,LOW);

  Mode_opening() 
}

void loop() {
  current_time = millis();

  if (current_time - previous_time < 2000){
    I_Stim = 0;
    Stim_state = Vm_min;
  }
  if (current_time - previous_time >= 2000){
    I_Stim = 50;
    Stim_state = Vm_max;
  }
  if (current_time -previous_time > 5000){
    previous_time = current_time;
  }
  
  v = v + timestep_ms*(0.04 * v * v + 5*v + 140 - u + I_Stim);
  u = u + timestep_ms*(a_Iziekevich * (b_Iziekevich * v - u));

  if (v >= Vm_peak){
    v = c_Iziekevich; 
    u = u + d_Iziekevich;
  }
  
  if (v <= Vm_min) {
    v = Vm_min; // Prevent pinVm going into overdrive - but also means that it will flatline at Vm_min. 
    } 
  
  //int AnalogOutValue = (v + 90) * 2;

  analogWrite(pinVm, map(v, Vm_min, 20, bits/4 ,bits));

//  if  (v > Vm_spike) {
//    spike=true;
//  }   
//
//  if (spike==true) {
//    digitalWrite(pinSpike, HIGH);
//    spike = false;
//  }
//  else {
//    digitalWrite(pinSpike, LOW);
//  }

  if  (v >= Vm_spike) {
    digitalWrite(pinSpike, HIGH);
  }   
  else {
    digitalWrite(pinSpike, LOW);
  }   
  
  Serial.print("Vm = ");
  Serial.print(v);
  Serial.print("\t");
//  Serial.print("spike = ");
//  Serial.print(spike);
//  Serial.print("\t");
//  Serial.print("I_Stim = ");
//  Serial.print(Stim_state);
//  Serial.print("\t");
  Serial.println("\t");
}


/////////////////////////////////////////////////////////

// From Iziekevich.org - see also https://www.izhikevich.org/publications/figure1.pdf:
//      0.02      0.2     -65      6       14 ;...    % tonic spiking
//      0.02      0.25    -65      6       0.5 ;...   % phasic spiking
//      0.02      0.2     -50      2       15 ;...    % tonic bursting
//      0.02      0.25    -55     0.05     0.6 ;...   % phasic bursting
//      0.02      0.2     -55     4        10 ;...    % mixed mode
//      0.01      0.2     -65     8        30 ;...    % spike frequency adaptation
//      0.02      -0.1    -55     6        0  ;...    % Class 1
//      0.2       0.26    -65     0        0  ;...    % Class 2
//      0.02      0.2     -65     6        7  ;...    % spike latency
//      0.05      0.26    -60     0        0  ;...    % subthreshold oscillations
//      0.1       0.26    -60     -1       0  ;...    % resonator
//      0.02      -0.1    -55     6        0  ;...    % integrator
//      0.03      0.25    -60     4        0;...      % rebound spike
//      0.03      0.25    -52     0        0;...      % rebound burst
//      0.03      0.25    -60     4        0  ;...    % threshold variability
//      1         1.5     -60     0      -65  ;...    % bistability
//        1       0.2     -60     -21      0  ;...    % DAP
//      0.02      1       -55     4        0  ;...    % accomodation
//     -0.02      -1      -60     8        80 ;...    % inhibition-induced spiking
//     -0.026     -1      -45     0        80];       % inhibition-induced bursting
  
