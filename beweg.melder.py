#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time

#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#Warnungenausschalten
GPIO.setwarnings(False)

#GPIO Pin Belegung
ROT    =13
GELB    =6
GRUEN   =5
TASTER =17
MELDER =12
#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(ROT,GPIO.OUT)#rot
GPIO.setup(GELB,  GPIO.OUT)#gelb
GPIO.setup(GRUEN, GPIO.OUT)#gruen
GPIO.setup(TASTER,GPIO.IN)#Taster
GPIO.setup(MELDER,GPIO.IN)#Bewegungsmelder

#Umschaltung definieren
def umschalten():
    #Phase 2
    GPIO.output(ROT,True)
    GPIO.output(GELB,True)
    GPIO.output(GRUEN,False)
    time.sleep(1)
    #Phase 3
    GPIO.output(GRUEN,True)
    
    GPIO.output(ROT,False)
    GPIO.output(GELB,False)
    time.sleep(2)
    #Phase 4
    GPIO.output(GELB,True)
    GPIO.output(GRUEN,False)
    time.sleep(1)
    #zurueck zu Phase 1
    GPIO.output(ROT,True)
    GPIO.output(GELB,False)
    #time.sleep(5)
    
    while True:
        #Phase 1
        GPIO.output(ROT,True)
        GPIO.output(GELB,False)
        GPIO.output(GRUEN,False)
        #Status des Tasters einlesen
        tasterStatus =GPIO.input(TASTER)
        melderStatus =GPIO.input(MELDER)
        if(tasterStatus or melderStatus):
            umschalten()
