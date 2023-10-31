# Codigo necesario para leer sensor led en los pines indicados ( 17 y 18 )
import RPi.GPIO as GPIO
import time

# Configuración de los pines GPIO
TRIG = 17  # Pin GPIO para el pulso de trigger
ECHO = 18  # Pin GPIO para el pulso de eco

# Configurar los pines como entrada o salida
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    while True:
        # Inicializa el sensor
        GPIO.output(TRIG, False)
        time.sleep(0.2)  # Espera un tiempo para estabilizar

        # Genera un pulso ultrasónico
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        # Espera a que el pulso de eco se active
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        # Espera a que el pulso de eco termine
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        # Calcula la duración del pulso de eco
        pulse_duration = pulse_end - pulse_start

        # Convierte la duración del pulso en distancia
        distance = pulse_duration * 17150  # Velocidad del sonido en cm/s

        # Redondea la distancia a dos decimales
        distance = round(distance, 2)

        # Imprime la distancia en el monitor
        print(f"Distancia: {distance} cm")

except KeyboardInterrupt:
    print("Medición finalizada")
    GPIO.cleanup()