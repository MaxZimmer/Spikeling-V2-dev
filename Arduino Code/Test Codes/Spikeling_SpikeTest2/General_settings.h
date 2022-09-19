/*          ---  General Settings  ---
*/


// // // // // // // // // // // // // // // // // // // // // // // //
/*                          Pin Definition                           */
int pinVmPot       =  12;        // Voltage clamp potentiometer pin
int pinLEDVm       =  18;        // Spike Red LED pin
int pinSpike       =  19;        // Green & Blue LEDs + Buzzer pin

int pinSyn1_D      =  32;        // Input Digital pin for Synapse 1
int pinSyn1_A      =  33;        // Input Analog pin for Synapse 1
int pinSyn1Pot     =  25;        // Synapse 1 Gain potentiometer pin

int pinSyn2_D      =  26;        // Input Digital pin for Synapse 2
int pinSyn2_A      =  27;        // Input Analog pin for Synapse 2
int pinSyn2Pot     =  14;        // Synapse 2 Gain potentiometer pin

int pinAxon_D      =  23;        // Output Digital pin for the axon
int pinAxon_A      =  36;        // OutputAnalog pin for the axon

int pinPD          =  15;        // Photodiode reading pin
int pinPDPot       =   2;        // Photodiode Gain potentiometer pin

int pinModeButton  =  21;        // Mode Button pin
int pinStim_D      =  22;        // Output Digital pin for the stimulating LED
int pinStim_A      =   1;        // Output Analog pin for the stimulating Current Input pin
int pinStimStrPot  =  34;        // Stimulus amplitude potentiometer pin
int pinStimFrePot  =  35;        // Stimulus frequency potentiometer pin
int pinCurrentIn   =   3;        // Input Analog pin for CurrentIn stimuli
int pinNoisePot    =  13;        // Noise generator potentiometer pin


// // // // // // // // // // // // // // // // // // // // // // // //
/*                         Neuron parameters                         */
int      Vm_min    = -90;        // Minimum voltage value the v variable from Izhikevich can take
int      Vm_spike  = -30;        // Voltage value above which the neuron will spike
int      Vm_peak   =  30;        // Voltage peak value from which the v variable will start its recovery
boolean  spike     = false;      // Boolean used for registrating spike events
float    I_Total;                // Sum of all applied current to the neuron (I_Vm, I_PD, I_Synapse1, I_Synapse2, I_Stim, I_Noise) 


// // // // // // // // // // // // // // // // // // // // // // // //
/*                     Voltage Clamp parameters                      */
int   Vm_Clamp;                  // Vm potentiometer value
int   VmPotScaling =  10;        // Vm_Clamp value scaling - The lower, the stronger the impact of the Vm potentiometer
float I_Vm;                      // "Current" value generated from the two previous variables in order to modify the holding voltage value


// // // // // // // // // // // // // // // // // // // // // // // //
/*                       Synapse1 parameters                         */
int SpikeIn1State;               // Synapse 1 digital input
int Syn1_Gain;                   // Synapse 1 gain potentiometer value
int Syn1PotScaling =  10;        // Synapse 1 gain sacaling - The lower, the stronger the impact of the Syn1_Potentiometer.  Default = 2
int Syn1_Amp;                    // Synapse 1 applied gain
int I_Synapse1;                  // Synapse 1 input current
int Synapse1_decay = 0.995;      // Synpase 1 decay rate. The difference to 1 matters - the smaller the difference, the slower the decay. Default  = 0.995


// // // // // // // // // // // // // // // // // // // // // // // //
/*                       Synapse2 parameters                         */
int SpikeIn2State;               // Synapse 2 digital input
int Syn2_Gain;                   // Synapse 2 gain potentiometer value
int Syn2PotScaling =  10;        // Synapse 2 gain sacaling - The lower, the stronger the impact of the Syn2_Potentiometer.  Default = 2
int Syn2_Amp;                    // Synapse 2 applied gain
int I_Synapse2;                  // Synapse 2 input current
int Synapse2_decay = 0.990;      // Synpase 2 decay rate. The difference to 1 matters - the smaller the difference, the slower the decay. Default  = 0.990


// // // // // // // // // // // // // // // // // // // // // // // //
/*                      PhotoDiode parameters                        */
int PDPotScaling  = 100;    // the lower, the stronger the impact of the Vm poti.  Default = 2
int PD_Gain;
int PD_Amp;
int PD_Value;
float PD_Scaling = 2.5;
int PD_Value_Array[] = {0,0,0,0,0,0,0,0,0,0};
int PD_counter = 0;
int PD_avg = 10;
int PD_Value_Sum;
int PD_Value_Average;
float PD_Decay = 0.001;
float PD_gain_mini = 0.0;  // the photodiode gain cannot decay below this value
float PD_Recovery = 0.001;
float I_PD;


// // // // // // // // // // // // // // // // // // // // // // // //
/*                        Stimuli parameters                         */
int StimStr_Value;               // Stimulus Strength potentiometer value
int StimStr;                     // Scaled stimulus strength
int Stim_minStr         = 5;     // Minimum stength value percentage below which the digital output is equal to 0
int Stim_val_D          = 0;     // Stimulus Digital output for stimulating LED
int Stim_val_A          = 0;     // Stimulus Analog output ofr Current in pin
int Stim_state;                  // Status of the stimulus (ON or OFF / 1 or 0);
int Stim_LEDScaling     = 40;    // Scaling applied to the digital out value
int Stim_CurrentScaling = 1000;  // Scaling applied to the analog out value

int StimFre_Value;               // Stimulus Frequency potentiometer value
int StimFre;                     // Scaled stimulus frequency
int Stim_counter = 0;            // Stimulus step counter (number of void loops)
int Stim_steps = 0;              // Number of steps required for half a stimulus duty cycle
int Stim_DutyCycle = 500;        // Default stinulus duty cycle value
int Stim_minDutyCycle = 10;      // Minimum loop steps the stimulus duty cycle cannot fall under

int Stim_State;
int CurrentIn_Value;             // Stimulus Current-In value read for the voltage clamp
int CurrentInScaling = 1000;
int I_Stim = 0;                  // Patch Current-In current


// // // // // // // // // // // // // // // // // // // // // // // //
/*                         Noise parameters                          */
int   Noise_Gain;                // Noise potentiometer value
int   NoiseScaling = 1000;       // Noise gain scaling - The lower, the stronger the impact of the Noise_Potentiometer.  Default = 1000
int   Noise_Amp;                 // Noise applied gain
float I_Noise;                   // Noise current


// // // // // // // // // // // // // // // // // // // // // // // //
/*                       Hardware parameters                         */
int BaudRate = 115200;
int bits = 4095;//1023;
int Mode = 0;
int ModeState = 0;

String   OutputStr;

void HardwareSettings(){
  //Serial.begin(BaudRate);

  pinMode(pinVmPot,INPUT);
  pinMode(pinLEDVm,OUTPUT);
  pinMode(pinSpike,OUTPUT);
  
  pinMode(pinSyn1_D,INPUT);
  pinMode(pinSyn1_A,INPUT);
  pinMode(pinSyn1Pot,INPUT);
  
  pinMode(pinSyn2_D,INPUT);
  pinMode(pinSyn2_A,INPUT);
  pinMode(pinSyn2Pot,INPUT);
  
  pinMode(pinAxon_D,OUTPUT);
  pinMode(pinAxon_A,OUTPUT);
  
  pinMode(pinPDPot,INPUT);
  pinMode(pinPD,INPUT);
  
  pinMode(pinModeButton,INPUT);
  
  pinMode(pinStimStrPot,INPUT);
  pinMode(pinStimFrePot,INPUT);
  pinMode(pinStim_D,OUTPUT);
  pinMode(pinStim_A,OUTPUT);
  pinMode(pinCurrentIn,INPUT);
  
  pinMode(pinNoisePot,INPUT);

  
  digitalWrite(pinLEDVm,LOW);
  digitalWrite(pinSpike,LOW);
  digitalWrite(pinAxon_D,LOW);
  digitalWrite(pinAxon_A,LOW);
  digitalWrite(pinStim_D,LOW);
  digitalWrite(pinStim_A,LOW);
}
