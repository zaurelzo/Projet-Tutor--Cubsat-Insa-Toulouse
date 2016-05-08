import serial
import time
import os

print("programme de test d'envoi :")
print("")

# configuration initiale
os.system("stty -F /dev/ttyAMA0 115200")
os.system("exec 9> /dev/ttyAMA0")

# variables
port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=1.0)
stay = True

# boucle principale
while stay:
        print("-> choix du protocole (UART/SPI) ?")
        choice = raw_input("")
        if choice=="UART":
                port.write("test")
                print("paquet transmis")
        elif choice=="SPI":
                os.system("./spidev_test -D /dev/spidev0.0")
        else :
                print("erreur")
        print ("-> relancer (Y/N) ?")
        ch = raw_input("")
        if ch=="N":
                stay = False
        time.sleep(0.5)