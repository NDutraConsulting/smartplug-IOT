from SmartSound import SmartSound
import RPi.GPIO as GPIO
from time import sleep

def main():
    pin =  13
    threshold = 25
    led = 0 # start state

    sound_sensor = SmartSound(GPIO_pin=5, MCP_ENV_PIN=4, MCP_AUD_PIN=3)
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    
    while(1):
        sleep(.01)
        if (sound_sensor.get_envelope() > threshold):
            if led:
                GPIO.output(pin, GPIO.LOW)
                led = 0
            else:
                GPIO.output(pin, GPIO.HIGH)
                led = 1


    
if __name__ == '__main__':
    main()
