#Aufgabe 3

import numpy as np
from skimage.io import imread, imsave
from skimage.util import random_noise
import matplotlib.pyplot as plt
from scipy.ndimage import convolve, filters

#from skimage.filters import 

#Aufgabe 3.1
einstein = plt.imread("einstein.png")

einstein2 = random_noise(einstein, mode = 'gaussian', var=0.01)

#plt.imshow(einstein2, cmap= "gray")

#Aufagbe 3.2

absolut = einstein
absolutVerrauscht = einstein2

absolutDifferenz = absolut - absolutVerrauscht


print("mittlere Differenz: " + str(np.abs(np.mean(absolutDifferenz))))

#Aufgabe 3.3

#Hier kann man die Größe des Arrays ändern
n = 3

#filterKern = [[0,0,(1/x)],[0,0,(1/x)],[0,0,(1/x)]]
nXn = np.zeros((n,n))
nXn += 1/(n * n)

boxFilternXn = convolve(einstein2, nXn , mode = 'reflect', cval = 1.0)


print(boxFilternXn)
plt.imshow(boxFilternXn, cmap='gray')

#Bei n=3 ist die Differenz = 0,48827.....(Beste praktische Ergebnis)
#Bis n=7 wird die Differenz größer und ab n=9 wird sie zunehmend wieder kleiner
faltungsDifferenz = np.mean((einstein - boxFilternXn))
print("Differenz Faltung: " + str(np.abs(faltungsDifferenz)))


#Aufgabe 3.4
#man sieht einen mathematischen Unterschied, aber die Ergebnisse sind alle sehr verrauscht (großer Unterschied sichtbar)
#beim Anzeigen von einem 3x3 Bild sieht man das Bild am besten

def Gauß(img):
    varianzEinstein = img
    i = 0.1
    minVarianz = 0
    minBerechnung = 1  
    while i <= 2.1:
        varianzEinstein = random_noise(img, mode = 'gaussian', var = i)
    
        berechnung = (np.abs(np.mean(varianzEinstein)))-(np.abs(np.mean(einstein)))
        print ("Varianz von i = " + str(round(i, 2)) + " hat die Differenz: " + str(berechnung))
        if berechnung < minBerechnung:
            minBerechnung = berechnung
            minVarianz = i
        
        i += 0.1
    
    varianzEinstein = random_noise(img, mode = 'gaussian', var = minVarianz)   
    print("Die kleinste Differenz ist bei i = " + str(round(minVarianz, 2)) + " mit dem Wert: " + str(minBerechnung)) 
    plt.imshow(varianzEinstein, cmap = "gray")
Gauß(einstein2)


#Aufgabe 3.5

einsteinSandP = random_noise(einstein, mode = 's&p')

plt.imshow(einsteinSandP, cmap= "gray")
Gauß(einsteinSandP)

#Aufgabe 3.6


