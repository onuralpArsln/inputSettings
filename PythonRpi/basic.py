from gpiozero import LED
from time import sleep 


led = LED(4)

for  i in range(4800):
	led.on()
	sleep(0.00001)
	led.off()
	sleep(0.00001)
	print(f"loop {i} ended")
