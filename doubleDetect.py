import evdev
import multiprocessing 




def listenEvent(deviceAdress, deviceNum):
    device=evdev.InputDevice(deviceAdress)
    for event in device.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            print(device.name)
            f = open("lastUsed.txt","w")
            f.write(deviceNum)
            f.close()


adres1="/dev/input/event4"
adres2="/dev/input/event16"


p1= multiprocessing.Process(target=listenEvent, args=(adres1,"1",))
p2= multiprocessing.Process(target=listenEvent, args=(adres2,"2",))
p1.start()
p2.start()
