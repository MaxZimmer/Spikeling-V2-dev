# Spikeling V 2.0


Spikeling V2.0 is an educational tool for neuroscience students and enthusiasts!

<p style='text-align: justify;'>
It is an artificial neuron that can receive different inputs, integrate them and send and outputs its computation, just like a spiking neuron would!

Technically, it consists on a microcontroller (an ESP32) running the computationally efficient Izhikevich model of a spiking neuron.
</p>

<div>

<p style='text-align: justify;'>
<img align="left" width="370" height="225" src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/Images/Spikeling_hardware.png">

<img align="left" width="369" height="225" src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/Images/Spikeling_GUI.gif">
</p>

</div>

***

<p style='text-align: justify;'>
<br>
If this all sounds familiar to you, it is because this project is a derivative (and update) of the Spikeling project started at the [BadenLab](https://badenlab.org/). With feedback from users and students, we are developing this version, which has added capabilities, and also revisits how lessons can be taught, and what kind of experiments can be done with it!

While this is not a stable version just yet, enthusiasts and potential collaborators can source the electronic bits for this project from [KitSpace](#)
</p


***

<p style='text-align: justify;'>
<img align="left" width="370" height="225" src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/Images/PCB.png">


<img align="left" width="370" height="225" src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/Images/Spikeling_front.png">
</p>


---

## Development log

#### Working Issues

GUI

Main issue concerns the live reading from the serial which is extremely slow (compared to the serial monitor on the arduion IDE). After trying for a time with the parent QtSerial, I switched to the most universal PySerial. Still the reading is waayyyyy too slow:

Here's just a few line that I run and that still gives me a slow serial read

```python
import serial

serialport = serial.Serial("COM11", 115200)
while True:
    rx = serialport.readline()
    rx_serial = str(rx, "utf-8").strip()
    v = rx_serial.split(",")
    print(v)
```

subsequently the live plotting is affected

***

Currently working on the 2.2 version.
It only incorporates slight component modification compared to version 2.1. These components are more widely found and a bit cheaper, therefore the modification.

Cost estimation spreadsheet
https://docs.google.com/spreadsheets/d/1JO1rpfb5DoqT5x59RL3RnkQFxRdzm5al6X8uEcsVFo8/edit#gid=0

This project is licensed under the [GNU General Public License v3.0](https://github.com/BadenLab/Openspritzer/blob/master/LICENSE)<br>
The hardware is licensed under the [CERN OHL v1.2](https://github.com/BadenLab/LED-Zappelin/blob/master/PCB/LICENSE)
