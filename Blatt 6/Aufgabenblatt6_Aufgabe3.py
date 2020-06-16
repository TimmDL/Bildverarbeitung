# Blatt 6 - Aufgabe 4

import numpy as np
import time
import matplotlib.pyplot as plt

from skimage.io import imread

# Teilaufgabe 1
bild1 = imread("bild1.png")
bild2 = imread("bild2.png")

hist1 = np.histogram(bild1,bins=256,range=(0,256))
hist2 = np.histogram(bild2,bins=256,range=(0,256))

plt.figure(1)
plt.hist(bild1.flatten(),bins=256,range=(0,256))

plt.figure(2)
plt.hist(bild2.flatten(),bins=256,range=(0,256))

# Teilaufgabe 2
def histogrammAusgleich(img):
    plt.figure(3)
    hist = np.histogram(img,bins=256,range=(0,256),density=True)
    plt.hist(img.flatten(),bins=256,range=(0,256),density=True)
    
    liste = np.zeros(255)
    for i in range(0,255):
        t = 255 * np.sum(hist[0][:i])
        liste[i] = t  
    
        

histogrammAusgleich(bild1)   
  
