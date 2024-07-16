from gpiozero import Button
from signal import pause

def say_hold():
    print("Hold down")

button = Button(17)
button.hold_time = 2
button.when_held = say_hold

pause()