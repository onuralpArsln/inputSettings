import evdev
import multiprocessing 




def listenEvent(deviceAdress):
    device=evdev.InputDevice(deviceAdress)
    for event in device.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            print(device.name)


adres1="/dev/input/event4"
adres2="/dev/input/event16"


p1= multiprocessing.Process(target=listenEvent, args=(adres1,))
p2= multiprocessing.Process(target=listenEvent, args=(adres2,))
p1.start()
p2.start()
