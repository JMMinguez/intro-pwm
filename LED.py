import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)

pwm = GPIO.PWM (11,100)
pwm.start (50)


input("Ejecutando hasta que se pulse una tecla")
pwm.stop ()

GPIO.cleanup ()
