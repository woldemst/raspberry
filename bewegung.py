#Import der Python Module
import RPi.GPIO as GPIO
import time

#Variablen definieren
PIR_Sensor = 23
LED = 24

#GPIOs mit GPIO-Nummer ansprechen
GPIO.setmode(GPIO.BCM)

#Ein- und Ausgaenge definieren
GPIO.setup(PIR_Sensor, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

print("Das Programm wurde gestartet.")

#Callback Funktion erstellen
def Bewegung(PIR_Sensor):
    print("Dein Electreeks Sensor hat eine Bewegung erkannt!")
    GPIO.output(LED, True)
    time.sleep(5)
    GPIO.output(LED, False)

#Hauptprogramm starten
if __name__ == "__main__":
    try:
        #Sobald eine Bewegung erkannt wurde, fuehre die Funktion aus.
        GPIO.add_event_detect(PIR_Sensor, GPIO.RISING, callback=Bewegung)
        while True:
            time.sleep(0)
        
    #Programm beenden mit Strg + c
    except KeyboardInterrupt:
        print ("Das Programm wurde beendet.")
        GPIO.cleanup()
