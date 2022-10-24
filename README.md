# Spikeling V 2.0


Spikeling V2.0 is an educational tool for neuroscience students and enthusiasts!

<p style='text-align: justify;'>
It is an artificial neuron that can receive different inputs, integrate them and send and outputs its computation, just like a spiking neuron would!

Technically, it consists on a microcontroller (an ESP32) running the computationally efficient Izhikevich model of a spiking neuron.
</p>

<div>


<img align="left" width="405" height="250" src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/Images/Spikeling_hardware.png">

<img align="left" width="405" height="250" src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/GUI/Pictures%20%26%20Logos/Spikeling_GUI.gif">


</div>
<br><br/>

***
<br><br/>

<div>
<p style='text-align: justify;'>
If this all sounds familiar to you, it is because this project is a derivative (and update) of the Spikeling project started at the <a href="https://badenlab.org">BadenLab</a>.
With feedback from users and students, we are developing this version, which has added capabilities, and also revisits how lessons can be taught, and what kind of experiments can be done with it!

While this is not a stable version just yet, enthusiasts and potential collaborators can source the electronic bits for this project from <a href="https://kitspace.org/boards/github.com/maxzimmer/spikeling-v2/">KitSpace</a></p>
</div>


***


<p style='text-align: justify;'>
<img align="left" width="370" height="225" src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/Images/PCB.png">

<p style='text-align: justify;'>
The main upgrade on the PCB concerns the use of an ESP32 module and 2 ADC 8bit expander chips that together allow spikeling to compute more input output with specific input/output ports and dedicated potentiometer. The previous version had limited ports and potentiometers and different functions had to be encoded on the arduino code hence impacting the versatility of the model.

Stereo (3-ways) audio jacks 3.5mm replace the previous BNC cable. Both ports and cables are therefore cheaper, also ports are less bulky and cables more flexible. Moreover, now one single port can carry two distinct information. In this case digital and analog input/output.

Since the user cannot access the microcontroler board anymore (acrylic sheet on top of the board), a reset button has been added to the back of the board.

Previously, "modes" were encoded manually on the microcontroler, and the user could check the set mode number by the amount of flashes the microcontroller built-in LED was providing at the begining of the routine.
Now, the microcontroller is pre-set with 12 distinct "neuron modes" that the user can switch through, 12 proxy LED indicate continuously which mode is currently being set.

The buzzer is now smaller and is powered by the ESP32 3.3V (instead of the 5v from the arduino), making its clicking noise quieter, which is more pleasant for the user ear, especially after a couple of minutes using the device.

A couple of functions have been added to the board and can now be controlled through potentiometers (synaptic polarity(inhibitory/excitatory), photoreceptor gain and polarity, stimulus strength and polarity(only for current input not LED stimulation))


<img align="left" width="370" height="225" src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/Images/Spikeling_front.png">
</p>


---

<br>
<div>

# Development log

### Working Issues

##### GUI

- Serial reading is slow and pyQtgraph does not update fast enough the serial values.

>FIXED: The entire code was reimplement using a lower BaudRate (9600 instead of 115200) and the pyQtgraph routine was improved.
Currently the GUI functions are being reimplemented with the PySerial readWrite functions. Updates to come.

##### PCB
- The audio jack footprint is not correct. the back pin and holes are mm ahead of their correct position.

>FIXED: the new PCB in the 2.2c version now posses the correct footprint. Previous version will need to cut the plastic pieces in front of the audio jack female and force the component into position

- The LEDs on the board might be to Bright

> The resistance of the 4 CharliePlex and the SpikeLed resistors must be adjusted to the acrylic material chosen for the front cover. The current 100 Ohm is sufficient for opaque PMMA, but clear transparent ones should have 1 kOhm soldered below so that the LEDs do not affect the user vision.

- The CharliePlex footprint orientation (+/-) is not labeled

</div>



***


Cost estimation spreadsheet for production
https://docs.google.com/spreadsheets/d/1JO1rpfb5DoqT5x59RL3RnkQFxRdzm5al6X8uEcsVFo8/edit#gid=0

This project is licensed under the [GNU General Public License v3.0](https://github.com/BadenLab/Openspritzer/blob/master/LICENSE)<br>
The hardware is licensed under the [CERN OHL v1.2](https://github.com/BadenLab/LED-Zappelin/blob/master/PCB/LICENSE)
