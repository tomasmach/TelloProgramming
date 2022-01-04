from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon() #Dron začne odesílat programu obraz

while True: #Nekonečný loop, program jede dokola
    img = me.get_frame_read().frame #Program začne zpracovávat každý frame obrazu
    img = cv2.resize(img,(360,240)) #V jakém rozlišení má program zpracovávat video z dronu
    #Obraz lze zvětšit, ovšem čím menší rozlišení, tím rychlejší program
    cv2.imshow("Image", img) #Vytvořím okno, ve kterém uvidím obraz z dronu
    cv2.waitKey(1) #Optimalizace kódu