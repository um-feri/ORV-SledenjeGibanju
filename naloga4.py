import cv2 as cv
import numpy as np

def meanshift(slika, lokacija_okna, iteracije, napaka):
    pass

if __name__ == "__main__":
    #Naloži video
    cap = cv.VideoCapture('video.mp4')
    #Preveri, če je video uspešno naložen
    if not cap.isOpened():
        print("Napaka: Video ne obstaja ali ni bil uspešno naložen.")
        exit(1)

    #Nastavitve meanshift algoritma
    iteracije = 10
    napaka = 1

    #Začetna točka sledenja
    x, y, w, h = 0, 0, 0, 0
    #Izračun značilnic za sledenje
    uspel, sablona = cap.read()

    #Začetek sledenja
    while True:
        uspel, slika = cap.read()
        if not uspel:
            break        
        cv.imshow('Slika', slika)
        okno = meanshift(slika, (x, y, w, h), 10, 1)
        #Nariši okno
        cv.rectangle(slika, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
