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
    # toDo : 이미지를 촬영하여 넘겨줌
    for i in range(0, 3):
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
