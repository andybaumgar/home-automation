#include <Stepper_28BYJ_48.h>

Stepper_28BYJ_48 small_stepper(D1, D3, D2, D4); //Initiate stepper driver



void setup(void)
{
  Serial.begin(115200);
  delay(100);
  Serial.print("Starting now\n");
  loop();
}


void loop(void)
{
    small_stepper.step(1);
}
