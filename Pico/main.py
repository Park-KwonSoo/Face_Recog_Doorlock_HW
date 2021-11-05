from machine import Pin, UART
from time import sleep

pirMotionSensor = Pin(14, Pin.IN)
uart = UART(0, 9600)

# pirMotionSensor 시작


def startPirMotion():
    while True:
        if(pirMotionSensor.value()):
            capturedImage = captureImage()
            for image in capturedImage:
                sendImage(image)
        sleep(.5)


def captureImage():
    yield 1


def sendImage(image):
    # toDo : Send Image
    print("sendingImage : ", image)
    uart.write(bytes(10*image))


def start():
    startPirMotion()


if __name__ == "__main__":
    print("hello World")
    start()
