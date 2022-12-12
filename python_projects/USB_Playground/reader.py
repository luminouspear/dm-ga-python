import usb.core
import usb.backend.libusb1

backend = usb.backend.libusb1.get_backend()
print(f'backend: {backend}')

device = usb.core.find(idVendor=0x045e,idProduct=0x0b00, backend=backend)

if device is None:
    raise ValueError('Device not found')

endpoint = device[0].interfaces()[0].endpoints[0]

interface = device[0].interfaces()[0].bInterfaceNumber
device.reset()

if device.is_kernel_driver_active():
    device.detach_kernel_driver()

device.set_configuration()
endpoint_address = endpoint.bEndpointAddress

reader = device.read(endpoint_address, 1024)
print(len(reader))
