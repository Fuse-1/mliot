import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
gpio.setup(3,OUT)
while True:
    gpio.output(3,True)
    time.sleep(0.5)
    gpio.output(3,False)
    time.sleep(0.5)
