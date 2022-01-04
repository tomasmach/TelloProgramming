from djitellopy import tello #Import knihovny
from time import sleep #Import knihovny

dronik = tello.Tello() #Vytvoření Tello objektu. Zjednodušení pro psaní
dronik.connect() #Připojení programu na dron
print(dronik.get_battery()) #Vypíše stav baterie dronu

dronik.takeoff() #Dron vzlétne

#dronik.move_forward(50) - Dron poletí 50cm dopředu, ale nemůžeme kontrolovat rychlost

#4 hodnoty. Doleva/Doprava, dopředu/dozadu, stoupání/klesání, otáčení dronu
dronik.send_rc_control(0, 50, 0, 0)
sleep(4)
#Dám dronu command a poté pozastavím program na 4 vteřiny, tudíž dron bude plnit co chci 4 vteřiny
dronik.send_rc_control(30, 0, 0, 0)
sleep(3)

dronik.send_rc_control(-30, 0, 0, 0)
sleep(3)

dronik.send_rc_control(0, 0, 0, 0) #Vynuluji commandy

dronik.land()