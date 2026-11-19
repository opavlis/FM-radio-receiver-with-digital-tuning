# FM radio receiver with digital tuning
This is a project for Digital Electronics 2 (BPC-DE2) on Brno University of Technology BUT FEEC.  
The goal of this project is to make a fully functional FM radion based on Raspberry PI Pico W.

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
![Will be added!](Images/Block_schematic.png)

## Testing individual components
### OLED Graphic Display Module 
- was tested by wiring in to breadboard, found on I2C bus and [printing text "Hello"](Images/Displaytestphoto.py) with a [simple code](Test_codes/Testcode_display.py).

## Timing/concurrency plan  
| **Week**| **Plan** |
|---|---|
| 1. | Team members, creating GitHub repository, approval on Block diagram / pinout |
| 2. | Testing modules / display, create complete wiring diagram  |
| 3. | Wiring of the entire circuit and putting it into operation  |
| 4. | Bug fixes, finishing documentation, making poster / short video  |
| 5. | Demonstration and defense |


