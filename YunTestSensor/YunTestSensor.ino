#include <Console.h>

int n = 0;

void setup() {
  Bridge.begin();
  Console.begin();
}

void loop() {
  // Output a sensor value.
  // Format is "name:value" where name is any string and value is an integer or float value.
  // Don't forget to end with println so a newline character is output at the end!
  Console.print("Sensor One:");
  Console.println(n);
  
  // Output another sensor value.
  Console.print("Sensor Two:");
  Console.println(10.0*sin((2.0*PI)/100.0*float(n)));
  
  // Increase the test sensor values.
  n += 1;
  if (n >= 99) {
    n = 0;
  }
  
  // Wait 10 seconds and output another measurement.
  // Make sure to wait at least a second or so between measurements so the bridge library
  // isn't flooded with requests.
  delay(10*1000);
}
