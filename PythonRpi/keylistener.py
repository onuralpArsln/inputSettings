from pynput import keyboard 
import time 

last_time =time.time()

with open("count.txt","r") as a:
    b=a.read().strip()
    b=int(b)
step=0
def on_keypress(key):
    global last_time
    global b
    global step
    if key== keyboard.Key.esc:
        return False
    try:
        k = key.char
    except:
        k=key.name

    if time.time() - last_time > 0.7:
        print(k)
        if k == "d":
            step +=1
            b+=1
        if step == 1000:
            step=0
            with open("count.txt","w") as a:
                a.write(str(b)) 
                print(b)
        
    last_time = time.time()

listener = keyboard.Listener(on_press=on_keypress)
listener.start()
listener.join()
