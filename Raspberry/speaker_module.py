import RPi.GPIO as GPIO
import time

SPEAKER = 21

def speakerRun(seconds):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SPEAKER, GPIO.OUT)
        speaker = GPIO.PWM(SPEAKER, 50)
        speaker.start(70)
        start = time.perf_counter()
        end = time.perf_counter()
        while 1:
            for x in range(200, 2200):
                speaker.ChangeFrequency(x)
                time.sleep(.0001)
                end = time.perf_counter()
            for x in range(200, 2000):
                speaker.ChangeFrequency(2200 - x)
                time.sleep(.0001)
                end = time.perf_counter()
            if(end - start >= seconds) :
                break;
    except KeyboardInterrupt:
        speaker.stop()
        GPIO.cleanup()
    finally :
        GPIO.cleanup()



if __name__ == "__main__":
    speakerRun(5)
