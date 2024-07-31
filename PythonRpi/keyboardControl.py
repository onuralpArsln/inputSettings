from pynput import keyboard 
from gpiozero import LED
from time import sleep 

motor = LED(4)
directionPin = LED(27)

def move(length=4800,direction=0,pinMot=motor,pinDir=directionPin):
    if direction==0:
        pinDir.on()
    else:
        pinDir.off()

    for  i in range(length):
	    motor.on()
	    sleep(0.00001)
	    motor.off()
	    sleep(0.00001)
	    print(f"loop {i} ended for direction {direction}")


move(1300,0)
move(1300,1)

def on_keypress(key):
    if key== keyboard.Key.esc:
        return False
    try:
        k = key.char
    except:
        k=key.name
    
    if "up" in k:
        move(1300,0)
    elif "down" in k:
        move(1300,1)
    print(k)

listener = keyboard.Listener(on_press=on_keypress)
listener.start()
listener.join()
