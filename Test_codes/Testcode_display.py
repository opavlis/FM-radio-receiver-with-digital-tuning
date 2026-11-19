from machine import Pin, I2C
import sh1106

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=100000)

if i2c.scan():
    print("Displej pripojen")
    oled = sh1106.SH1106_I2C(i2c, 128, 64)
    oled.text("Hello", 50, 28, 1)
    oled.show()
else:
    print("Chyba: Nenalezen.")