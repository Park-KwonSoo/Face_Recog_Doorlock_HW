import bluetooth
import io
from time import ctime as now
from PIL import Image, ImageFile

import http_requests_module  # 이미지를 서버로 전송하기 위한 모듈

ImageFile.LOAD_TRUNCATED_IMAGES = True
target_device = "20:19:07:00:77:2E"
port = 1

socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
socket.connect((target_device, port))

print("socket connected")


def getBytesStream(socket, length):
    buf = b''
    try:
        step = length
        while True:
            data = socket.recv(step)
            buf += data
            if len(buf) == length:
                break
            elif len(buf) < length:
                step = length - len(buf)

    except Exception as e:
        print(e)

    return buf


while True:
    length = int.from_bytes(socket.recv(3), 'big')
    if length:
        print('Camera capture start...')
        data = getBytesStream(socket, length)
        stream = io.BytesIO(data)
        fileName = '-'.join(now().split(' ')) + '.jpeg'
        img = Image.open(stream)
        img.save(fileName)
        print('Image {0} is saved'.format(fileName))
        http_requests_module.photoSend(fileName)
