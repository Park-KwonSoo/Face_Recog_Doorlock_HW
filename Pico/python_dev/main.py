from time import sleep
import board
import busio
from CameraModule import getImage
from digitalio import DigitalInOut, Direction

pirMotionSensor = DigitalInOut(board.GP15)
pirMotionSensor.direction = Direction.INPUT
uart = busio.UART(tx=board.GP0, rx=board.GP1)


def startPirMotion():
    while True:
        if(pirMotionSensor.value):
            capturedImage = captureImage()
            for image in capturedImage:
                sendImage(image)
            sleep(10)
        sleep(.5)


def captureImage():
    # toDo : 이미지를 촬영하여 넘겨줌
    # for i in range(0, 3):
    #     sleep(1)
    #     yield i
    result = getImage()
    for image in result:
        yield image


def sendImage(image):
    # toDo : Send Image
    print("sendingImage : ", image)
    uart.write(bytes(10*image))


def start():
    startPirMotion()


if __name__ == "__main__":
    print("hello World")
    start()
