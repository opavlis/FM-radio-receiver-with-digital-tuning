# FM-radio-receiver-with-digital-tuning
This is a project for Digital Electronics 2 (BPC-DE2) on Brno University of Technology BUT FEEC.

## Team members
+ **Martin Morávek** - *SW engineer + documentation*
+ **Adrian Munteanu** - *SW engineer and design*
+ **Antonín Navrkal** - *HW and SW engineer*
+ **Ondřej Pavliš** - *HW and SW engineer + documentation*

## Components used
+ Raspberry Pi Pico W
+ OLED Graphic Display Module
+ Rotary encoder
+ FM STEREO modul Si4703
+ Potentiometer
+ 2x Buttons

## Block schematic
![Popis obrázku](Images/Block_schematic.png)

## Pin/Bus plan

| Periferie | Signal | GPIO / Pin |
|---|---|---|
| **Si4703 FM modul** | SDIO  | GP4  |
| | SCLK  | GP5  |
| | RST | GP6 |
| | GPIO2  | GP7 |
| | VIN | 3V3 |
| | GND | GND |
| **OLED display** | SDA | GP4  |
| | SCL | GP5  |
| | VCC | 3V3 |
| | GND | GND |
| **Potentiometer** | Middle pin | GP26  |
| | Left pin | 3V3 |
| | Right pin | GND |
| **Rotary encoder** | CLK  | GP8 |
| | DT  | GP9 |
| | SW  | GP10 |
| | + | 3V3 |
| | GND | GND |
| **Button 1** | IN | GP11 |
| | OUT | GND |
| **Button 2** | IN | GP12 |
| | OUT | GND |

##


