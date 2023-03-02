from machine import Pin
import dht, time

pin_04=dht.DHT22(Pin(4))

while True:
    pin_04.measure()
    temperatura = pin_04.temperature()
    humedad = pin_04.humidity()
    print("Temperatura: " + str(temperatura) + "°C")
    print("Humedad: " + str(humedad) + "%")
    time.sleep(5)
    
