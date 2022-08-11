# Spikeling V 2.0

### To be modified for V 2.1

- RGB LED

      The soldered LEDs have common anode and therefore do not correspond to the PCB schematics (common cathode).

      The PCB footprint is as follow: GND, R, G, B (may consider changing for R, GND, G, B which is more common)

      The LEDs G and B should have their own analog pin and not be dependent of the buzzer digital pin.

      On the PCB, invert GND and VCC on all pot
      on PCB change writing on noise potentiometer
