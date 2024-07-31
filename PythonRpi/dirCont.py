
from gpiozero import LED
from time import sleep 


motor = LED(4)
directionPin = LED(27)
with open("press.txt","r") as a:
    b=a.read().strip()
    b=int(b)

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
        #print(f"loop {i} ended for direction {direction}")
step=0
while True:
    sleep(0.4)
    move(1300,1)
    sleep(0.4)
    move(1300,0)
    b +=1 
    step +=1
    print(b)
    if step == 1000:
        step=0
        with open("press.txt","w") as a:
            a.write(str(b))
