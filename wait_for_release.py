from gpiozero

button = Button(17)

while True:
    button.wait_for_press()
    print("Button is pressed")

    button.wait_for_release()
    print("Button is released")