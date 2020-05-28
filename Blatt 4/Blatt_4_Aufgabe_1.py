# Blatt 4 - Aufgabe 1

import numpy as np

from skimage.io import imread

import matplotlib.pyplot as plt
import math as m


# Aufgabe 1
bild1 = plt.imread("bild1.png")
bild2 = plt.imread("bild2.png")
bild3 = plt.imread("bild3.png")


def logImg(img):
    log = 255/(np.log(1 + np.max(img)))  * np.log(1 + img) 
  
    log = np.array(log, dtype = np.uint8) 
    return log

def powerImg(img):  
      
    gamma = np.array(255*(img / 255) ** 0.5, dtype = 'uint8') 
    return gamma

def threshold(img):
    thresh = 0.4
    row, column = img.shape
    for i in range(row):
        for j in range(column):
            if img[i,j] > thresh:
                img[i,j] = 1
    return img            
            

# Aufgabe 1.1
#Gamma reduction kann für zu dunkle Bilder verwendet werden um diese zu erhellen.
# In der unteren linken Ecke des Bildes sind sieben Poller zu sehen
bild = powerImg(bild1)
plt.imshow(bild,cmap="gray")

# Aufgabe 1.2
# Die logarithmische Tranformation kann benutzt werden um den Kontrast zu erhöhen,
# da sie Werte, die nah aneinander sind auf einen größeren Wertebereich skaliert

bild = logImg(bild2)
plt.imshow(bild,cmap="gray", vmin=150, vmax=255)

#Aufgabe 1.3
# Wir verwenden Thresholding um nur den hellen Bereich im Bild (die Straße)
# auf weißes zu setzten. Ohne else statement wird der Rest des Bildes, wie in der Aufgabe gefordert,
# nicht verändert

bild3  = bild3[:,:,1]
bild = threshold(bild3)
plt.imshow(bild3 ,cmap="gray")






