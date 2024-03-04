from evdev import list_devices, InputDevice
devices = [InputDevice(dev) for dev in list_devices()]
for device in devices:
    print("Device:", device.name, "  Device path:", device.fn)
