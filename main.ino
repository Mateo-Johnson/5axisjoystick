#include <Arduino.h>

int joyX = A0;
int joyY = A1;
int xVal, yVal;

void setup() {
  Serial.begin(9600);
  pinMode(joyX, INPUT);
  pinMode(joyY, INPUT);
}

void loop() {
  xVal = analogRead(joyX);
  yVal = analogRead(joyY);
  Serial.print(xVal);
  Serial.print(",");
  Serial.println(yVal);
  delay(100);
}
