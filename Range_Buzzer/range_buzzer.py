# https://electrosome.com/hc-sr04-ultrasonic-sensor-raspberry-pi/
import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
#GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 
GPIO.setmode(GPIO.BOARD)
#TRIG = 23                                  #Associate pin 23 to TRIG
#ECHO = 24                                  #Associate pin 24 to ECHO

TRIG = 16                                  #Associate pin 23 to TRIG
ECHO = 18                                  #Associate pin 24 to ECHO

print "Distance measurement in progress"

GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in

#Buzzer
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
beepCounter = 1000
while True:

  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  print "Waitng For Sensor To Settle"
  time.sleep(2)                            #Delay of 2 seconds

  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points

  #if distance > 2 and distance < 400:      #Check whether the distance is within range
    #print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
  dis_cm = distance - 0.5
  dis_inch = dis_cm * 0.393701
  print "Distance:",dis_inch," inch"

  if dis_inch < 10:
      print "Distance inside IF:",dis_inch," inch"
      
      print "Beep ON"
      GPIO.setup(7,GPIO.OUT) # setup makes buzzer activates
      
  else:
      print "Beep OFF"
      
      #beepCounter = 0
  #else:
    #print "Out Of Range"                   #display out of range
