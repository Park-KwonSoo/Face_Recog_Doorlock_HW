import RPi.GPIO as GPIO
import time

SOLENOID = 17


def solenoidRun():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SOLENOID, GPIO.OUT)
        while 1:
            GPIO.output(SOLENOID, 1)
            print('solenoid Run', SOLENOID)
            time.sleep(1)
            GPIO.output(SOLENOID, 0)
            print('solenoid Stop', SOLENOID)
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    solenoidRun()
