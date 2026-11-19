# FM radio receiver with digital tuning
This is a project for Digital Electronics 2 (BPC-DE2) on Brno University of Technology BUT FEEC.  
The goal of this project is to make a fully functional FM radio based on Raspberry Pi Pico W.

## Project functionality
A rotary encoder will adjust the FM module frequency, and pressing it will allow you to save the selected frequency to memory. By pressing button 1 or 2, you can switch between the saved frequencies. A potentiometer will be used to control the radio's volume. Both the frequency and the volume will be displayed on an OLED screen. If possible, the name of the radio station or the currently playing song will also be shown.

## Team members
+ **Martin Morávek** - *SW engineer + documentation* (Block schematic, rotary encoder, FM module and potentiometer testing, pinout)
+ **Adrian Munteanu** - *SW engineer and design* (Wiring diagram, photos/videos shooting, pinout)
+ **Antonín Navrkal** - *HW and SW engineer* (FM module and OLED display testing, pinout)
+ **Ondřej Pavliš** - *HW and SW engineer + documentation* (GitHub repository, FM module testing, pinout)

## Components used and Pin/Bus plan
| Raspberry Pi Pico W |
| :--- | 
| <img src="Images/RPi.png" alt="Raspberry Pi Pico W" width="300"> |

| OLED Graphic Display Module | Signal  ->  GPIO / Pin |
| :--- | :--- |
| <img src="Images/OLEDdisplay.png" alt="OLED" width="300"> | SDA    ->    GP4<br>SCL    ->    GP5<br>VCC    ->    3V3<br>GND    ->    GND |


| Rotary encoder | Signal  ->  GPIO / Pin |
| :--- | :--- |
| <img src="Images/Rotaryencoder.png" alt="OLED" width="300"> | CLK    ->    GP16<br>DT    ->    GP17<br>SW    ->    GP15<br>+    ->    3V3<br>GND    ->    GND |


| FM STEREO module Si4703 | Signal -> GPIO / Pin |
| :--- | :--- |
| <img src="Images/FMradiomodule.png" alt="FM STEREO module Si4703" width="300"> | SDIO   ->   GP4<br>SCLK   ->   GP5<br>RST   ->   GP6<br>GPIO2   ->   GP7<br>VIN   ->   3V3<br>GND   ->   GND |

| Potentiometer | Signal -> GPIO / Pin |
| :--- | :--- |
| <img src="Images/Potentiometer.png" alt="Potentiometer" width="300"> | Middle pin   ->   GP26<br>Left pin   ->   3V3<br>Right pin   ->   GND |

| 2x Buttons | Signal -> GPIO / Pin |
| :--- | :--- |
| <img src="Images/button.png" alt="Button" width="300"> | **Button 1**<br>IN   ->   GP11<br>OUT   ->   GND<br><br>**Button 2**<br>IN   ->   GP12<br>OUT   ->   GND |

## Block diagram
![Block diagram](Images/Block_schematic.png)

## Wiring diagram
![Wiring diagram](Images/Wirediagram.png)

## Testing individual components
### OLED Graphic Display Module 
- tested by wiring it to a breadboard, detecting it on the I2C bus and [displaying the text "Hello"](Images/Displaytestphoto.jpeg) using a [simple script](Test_codes/Testcode_display.py).

### FM STEREO module Si4703  
- similary to the Graphic Display this module was tested by [wiring it to a breadboard](Images/FMtest_photo.jpeg), detecting it on the I2C bus and [trying the radio connection](Images/FMtest.png) with a [script](Test_codes/Testcode_FMmodule.py). A library for the Si4703 chip was required for this task. 

### Rotary encoder 
- connected to Raspberry Pi Pico W and a [script](Test_codes/Testcode_encoder.py)  was used to monitor how the encoder's rotation value changes.

### Potentiometer
- also connected to Raspberry Pi Pico W, ADC values were monitored and then recalculated in [script](Test_codes/Testcode_potentiometer.py) to [show in volts](Encodertest.mp4).

## Timing/concurrency plan  
| **Week**| **Plan** |
|---|---|
| 1. | Team members, creating GitHub repository, approval on Block diagram / pinout |
| 2. | Testing modules / display, create complete wiring diagram  |
| 3. | Wiring of the entire circuit and putting it into operation  |
| 4. | Bug fixes, finishing documentation, making poster / short video  |
| 5. | Demonstration and defense |


