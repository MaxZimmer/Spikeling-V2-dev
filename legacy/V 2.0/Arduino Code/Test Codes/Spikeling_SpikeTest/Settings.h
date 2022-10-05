int pinVm = 18;          // Spike Red LED pin
int pinSpike = 19;       // Green & Blue LEDs + Buzzer pin

int pinModeButton = 21;  // Mode Button pin
int pinCP1 = 5;          // CharliePlexing pin 1
int pinCP2 = 17;         // CharliePlexing pin 2
int pinCP3 = 16;         // CharliePlexing pin 3
int pinCP4 = 4;          // CharliePlexing pin 4

int BaudRate = 9600;


int bits = 1023;


float timestep_ms     = 0.2;  // default 0.1. This is the "intended" refresh rate of the model.
float a_Iziekevich = 0.02; // time scale of recovery variable u. Smaller a gives slower recovery
float b_Iziekevich = 0.2;// recovery variable associated with u. greater b coules it more strongly 
float c_Iziekevich = -65; // after spike reset value
float d_Iziekevich = 8;// after spike reset of recovery variable
