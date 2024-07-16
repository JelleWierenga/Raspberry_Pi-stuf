from gpiozero import Button
from signal import pause

def say_pressed():
    print("Button is pressed")

button = Button(17)
button.when_pressed = say_pressed

pause()