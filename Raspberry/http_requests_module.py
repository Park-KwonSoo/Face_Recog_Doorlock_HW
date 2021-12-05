import requests
import os

import speaker_module
import solenoid_module

URL = "http://3.34.168.179:9900/image/faceRecognition"


def photoSend(photo):
    file = open(photo, 'rb')
    upload = {'image': file}
    response = requests.post(URL, files=upload, headers={
        'Connection': "keep-alive",
        "Content-Type": "image/jpeg"
    })
    print(response.status_code)
    if(response.status_code == 200):
        solenoid_module.solenoidRun()
    elif (response.status_code == 400):
        speaker_module.speakerRun(5)
    os.remove('./' + photo)
    print('{0} is removed'.format(photo))
