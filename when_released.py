from gpiozero import Button
from signal import pause

def say_released():
    print("Button is released")

button = Button(17)
button.when_released = say_released

pause()