import RPi.GPIO as GPIO
import time
from gpiozero import Buzzer
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#buzzer initialization
buzzer = Buzzer(16)
buzzerFlag = False
#buzzer.beep()
while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed 2')
        buzzerFlag = not buzzerFlag
        print "",buzzerFlag
        time.sleep(0.2)
        
    else:
        #print('Button not pressed')
        pass
    
    #Buzzer Active/Inactive
    if buzzerFlag:
        #print "Turning on Buzzer"
        buzzer.on()
        #buzzer.beep()
        sleep(1)
    else:
        #print "Turning off Buzzer"
        buzzer.off()
        #sleep(1)

