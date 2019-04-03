import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# ------------------------------------------
# PIN NUMARALARI
# ------------------------------------------
TRIG = 23
ECHO = 24

print("HC-SR04 mesafe sensoru")

# ------------------------------------------
# GİRİŞ VE ÇIKIŞLARIN BELİRTİLMESİ
# ------------------------------------------
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# ------------------------------------------
# MESAFE ÖLÇÜMÜ
# ------------------------------------------
while True:
    # ölçme aralığı ve veri iletim hızı
    GPIO.output(TRIG, False)
    print("Olculuyor...")
    time.sleep(0.5)

    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)

    # 2 ve 400 aralığındaki ölçümler yapılır onun dışında menzil aşıldı bilgisi verilir
    if distance > 2 and distance < 400:
        print("Mesafe:", distance - 0.5, "cm")
    else:
        print("Menzil asildi")
