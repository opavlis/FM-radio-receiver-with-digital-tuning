from machine import Pin, I2C
import time
import si4703

rst = Pin(6, Pin.OUT)
sdio = Pin(18, Pin.OUT)

sdio.value(0)
rst.value(0)
time.sleep(0.1)
rst.value(1)
time.sleep(0.1)

i2c = I2C(1, scl=Pin(19), sda=Pin(18), freq=100000)

addresses = i2c.scan()
print("Found I2C adresses:", addresses)

try:
    radio = si4703.Si4703(i2c)
    
    radio.set_volume(15)

    radio.set_frequency(92.6) 
    
    print("DONE! Radio is playing")

except Exception as e:
    print("ERROR:", e)