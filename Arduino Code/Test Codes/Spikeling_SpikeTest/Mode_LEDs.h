#include Settings

int Mode_LED = 0;

int CPtime = 100;

bool Mode_flag;


#define PIN_CONFIG 0
#define PIN_STATE 1
#define LED_Num 12

int matrix[LED_Num][2][4] = {

  //           PIN_CONFIG                  PIN_STATE
  //    A       B       C      D         A     B    C    D
  { { OUTPUT, OUTPUT, INPUT, INPUT }, { HIGH, LOW, LOW, LOW } }, 
  { { OUTPUT, OUTPUT, INPUT, INPUT }, { LOW, HIGH, LOW, LOW } }, 
  { { INPUT, OUTPUT, OUTPUT, INPUT }, { LOW, HIGH, LOW, LOW } },
  { { INPUT, OUTPUT, OUTPUT, INPUT }, { LOW, LOW, HIGH, LOW } }, 
  { { INPUT, INPUT, OUTPUT, OUTPUT }, { LOW, LOW, HIGH, LOW } },
  { { INPUT, INPUT, OUTPUT, OUTPUT }, { LOW, LOW, LOW, HIGH } }, 
  { { OUTPUT, INPUT, OUTPUT, INPUT }, { HIGH, LOW, LOW, LOW } }, 
  { { OUTPUT, INPUT, OUTPUT, INPUT }, { LOW, LOW, HIGH, LOW } }, 
  { { INPUT, OUTPUT, INPUT, OUTPUT }, { LOW, HIGH, LOW, LOW } }, 
  { { INPUT, OUTPUT, INPUT, OUTPUT }, { LOW, LOW, LOW, HIGH } }, 
  { { OUTPUT, INPUT, INPUT, OUTPUT }, { HIGH, LOW, LOW, LOW } }, 
  { { OUTPUT, INPUT, INPUT, OUTPUT }, { LOW, LOW, LOW, HIGH } }  

};

void lightOn( int led ) {
  pinMode( CP1, matrix[led][PIN_CONFIG][0] );
  pinMode( CP2, matrix[led][PIN_CONFIG][1] );
  pinMode( CP3, matrix[led][PIN_CONFIG][2] );
  pinMode( CP4, matrix[led][PIN_CONFIG][3] );
  digitalWrite( CP1, matrix[led][PIN_STATE][0] );
  digitalWrite( CP2, matrix[led][PIN_STATE][1] );
  digitalWrite( CP3, matrix[led][PIN_STATE][2] );
  digitalWrite( CP4, matrix[led][PIN_STATE][3] );
}

void Mode_opening() {
  for( int l = 0; l < LED_Num; l++ ) {
    lightOn( l );
    delay(CPtime);
  }
  pinMode(CP1,INPUT);
  pinMode(CP2,INPUT);
  pinMode(CP3,INPUT);
  pinMode(CP4,INPUT);
}
