from gpiozero

button = Button(17)

button.wait_for_press()
print("Button is pressed")