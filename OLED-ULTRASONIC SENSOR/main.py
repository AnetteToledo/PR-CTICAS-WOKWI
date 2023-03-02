from machine import Pin,I2C
from HC_SR04 import HCSR04
import SSD1306
 
i2c = I2C(scl=Pin(13), sda=Pin(12), freq=100000)      #Init i2c
lcd=SSD1306.SSD1306_I2C(128,64,i2c) 
 
sensor = HCSR04(trigger_pin=22, echo_pin=21,echo_timeout_us=1000000)
 
try:
  while True:
    distance = sensor.distance_cm()
    print(distance)
    lcd.fill(0)
    lcd.text("Distance:",36,20) 
    lcd.text(str(distance),30,40)
    lcd.show()
except KeyboardInterrupt:
       pass    