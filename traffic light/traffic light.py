import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

red_led = 17
yellow_led = 27
green_led = 22

GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(yellow_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

GPIO.output(red_led, GPIO.HIGH)
time.sleep(2)

GPIO.output(red_led, GPIO.LOW)
GPIO.output(yellow_led, GPIO.HIGH)
time.sleep(2)

GPIO.output(yellow_led, GPIO.LOW)
GPIO.output(green_led, GPIO.HIGH)
time.sleep(2)

GPIO.output(green_led, GPIO.LOW)

GPIO.cleanup()