from machine import Pin
from time import sleep

#Setup Pin de Entrada (Pulsador)
pin_btn_up = Pin(19, Pin.IN, Pin.PULL_UP)
pin_btn_down = Pin(25, Pin.IN, Pin.PULL_UP)

#Setup Pines de Salida (Display Anodo Comun)
pin_a = Pin(13, Pin.OUT)
pin_b = Pin(12, Pin.OUT)
pin_c = Pin(14, Pin.OUT)
pin_d = Pin(2, Pin.OUT)
pin_e = Pin(4, Pin.OUT)
pin_f = Pin(5, Pin.OUT)
pin_g = Pin(18, Pin.OUT)
pin_dp = Pin(26, Pin.OUT)

#Estados logicos de ON/OFF para display de Anodo Comun
H = 0
L = 1
numero = 0

#Funcion para activar cada segmentos del display
def driver(a,b,c,d,e,f,g,dp):
    pin_a.value(a)
    pin_b.value(b)
    pin_c.value(c)
    pin_d.value(d)
    pin_e.value(e)
    pin_f.value(f)
    pin_g.value(g)
    pin_dp.value(dp)

#Funcion para pruebas de conexion y funcionamiento
def funcionamiento():
    driver(H, H, H, H, H, H, H, H)
    sleep(1)
    driver(L, L, L, L, L, L, L, L)

#Funcion que compara cada numero
def numeros(numero):
    #Numero 0
    if numero == 0:
        driver(H, H, H, H, H, H, L, L)
    #Numero 1
    if numero == 1:
        driver(L, H, H, L, L, L, L, L)
    #Numero 2
    if numero == 2:
        driver(H, H, L, H, H, L, H, L)
    #Numero 3
    if numero == 3:
        driver(H, H, H, H, L, L, H, L)
    #Numero 4
    if numero == 4:
        driver(L, H, H, L, L, H, H, L)
    #Numero 5
    if numero == 5:
        driver(H, L, H, H, L, H, H, L)
    #Numero 6
    if numero == 6:
        driver(H, L, H, H, H, H, H, L)
    #Numero 7
    if numero == 7:
        driver(H, H, H, L, L, L, L, L)
    #Numero 8
    if numero == 8:
        driver(H, H, H, H, H, H, H, L)
    #Numero 9
    if numero == 9:
        driver(H, H, H, H, L, H, H, L)

#Prueba de conexion y funcionamiento
funcionamiento()
numeros(numero)

#Bucle de repeticion infinita
while 1:
    #Si el estado del Pin de entrada up es LOW
    if (pin_btn_up.value() == 0):
        #Retardo Antirrebote
        sleep(0.005)
        #Mientras el estado del Pin sea LOW ingresa al bucle
        while(pin_btn_up.value() == 0):
            continue
        #Incrementa la variable en una unidad
        numero = numero+1
        #Si el valor de numero es mayor a 9
        if numero > 9:
            #Asigna el valor 0 a numero
            numero = 0
        #Envia a la funcion el valor de numero
        numeros(numero)
    #Si el estado del Pin de entrada down es LOW
    if (pin_btn_down.value() == 0):
        #Retardo Antirrebote
        sleep(0.005)
        #Mientras el estado del Pin sea LOW ingresa al bucle
        while(pin_btn_down.value() == 0):
            continue
        #Decrementa la variable en una unidad
        numero = numero-1
        #Si el valor de numero es menor a 0
        if numero < 0:
            #Asigna el valor 9 a numero
            numero = 9
        #Envia a la funcion el valor de numero
        numeros(numero)
    #Retardo 100ms
    sleep(0.1)