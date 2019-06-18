
import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM) #bcm 7 (bcm mode) and if board (26)
gpio.setup (7,gpio.OUT)
gpio.setup (23,gpio.OUT)

while True:
    gpio.output(7,1)
    print ("LED is ON")
    gpio.output(23,0)
    print ("LED is OFF")
    time.sleep(5)
    
    gpio.output(7,0)
    print ("LED is OFF")
    gpio.output(23,1)
    print ("LED is ON")
    time.sleep (5) #it is in seconds
    
