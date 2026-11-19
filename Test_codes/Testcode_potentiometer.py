from machine import ADC
from time import sleep

# ADC on pin GP26
pot = ADC(26)

while True:
    value = pot.read_u16()  # 0 to 65535
    voltage = value * 3.3 / 65535

    print("ADC:", value, "Voltage:", round(voltage, 2), "V")

    sleep(0.5)
