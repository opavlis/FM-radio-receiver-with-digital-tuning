
from machine import Pin
from time import sleep_ms

clk = Pin(16, Pin.IN, Pin.PULL_UP)
dt = Pin(17, Pin.IN, Pin.PULL_UP)
sw = Pin(15, Pin.IN, Pin.PULL_UP)

last_clk = clk.value()
position = 0

while True:
    current_clk = clk.value()

    if sw.value() == 0:
      print("Button pressed")

    if current_clk != last_clk:
        if dt.value() != current_clk:
            position += 1
            print("Right  | Position:", position)
        else:
            position -= 1
            print("Left   | Position:", position)

    last_clk = current_clk
    sleep_ms(2)
