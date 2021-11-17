import time as utime
import usb_cdc
from Arducam import *

once_number = 128
mode = 0
start_capture = 0
stop_flag = 0
data_in = 0
value_command = 0
flag_command = 0
buffer = bytearray(once_number)

mycam = ArducamClass(OV2640)
mycam.Camera_Detection()
mycam.Spi_Test()
mycam.Camera_Init()
mycam.OV2640_set_JPEG_size(OV2640_800x600)
utime.sleep(1)
mycam.clear_fifo_flag()


def imageCapture():
    count = 0
    length = mycam.read_fifo_length()

    mycam.SPI_CS_LOW()
    mycam.set_fifo_burst()
    while True:
        mycam.spi.readinto(buffer, start=0, end=once_number)
        usb_cdc.data.write(buffer)
        yield (bytearray(buffer))
        utime.sleep(.00015)
        count += once_number
        if count + once_number > length:
            count = length - count
            mycam.spi_readinto(buffer, start=0, end=count)
            usb_cdc.data.write(buffer)
            yield (bytearray(buffer))
            mycam.SPI_CS_HIGH()
            mycam.clear_fifo_flag()
            break


def getImage():
    mycam.start_capture()
    return imageCapture()
