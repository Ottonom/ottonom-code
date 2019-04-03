import RPi.GPIO as GPIO
import time
def ileri():
    GPIO.output("""solMotorGeri""",GPIO.LOW)
    GPIO.output("""solMotorİleri""",GPIO.HIGH)
    GPIO.output("""sagMotorGeri""",GPIO.LOW)
    GPIO.output("""sagMotorİleri""",GPIO.HIGH)

def geri():
    GPIO.output("""solMotorGeri""",GPIO.HIGH)
    GPIO.output("""solMotorİleri""",GPIO.LOW)
    GPIO.output("""sagMotorGeri""",GPIO.HIGH)
    GPIO.output("""sagMotorİleri""",GPIO.LOW)

def sag():
    GPIO.output("""solMotorGeri""",GPIO.LOW)
    GPIO.output("""solMotorİleri""",GPIO.HIGH)
    GPIO.output("""sagMotorGeri""",GPIO.HIGH)
    GPIO.output("""sagMotorİleri""",GPIO.LOW)

def sol():
    GPIO.output("""solMotorGeri""",GPIO.HIGH)
    GPIO.output("""solMotorİleri""",GPIO.LOW)
    GPIO.output("""sagMotorGeri""",GPIO.LOW)
    GPIO.output("""sagMotorİleri""",GPIO.HIGH)

def dur():
    GPIO.output("""solMotorGeri""",GPIO.LOW)
    GPIO.output("""solMotorİleri""",GPIO.LOW)
    GPIO.output("""sagMotorGeri""",GPIO.LOW)
    GPIO.output("""sagMotorİleri""",GPIO.LOW)

def geri_don():
    dur()
    time.sleep(1)
    sag()
    time.sleep(0.8)
    dur()