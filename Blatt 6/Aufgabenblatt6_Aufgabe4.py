# Blatt 6 - Aufgabe 4

import numpy as np
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
    hist = np.histogram(img,bins=256,range=(0,256),density=True)
    
    liste = np.zeros(256)
    for i in range(0,256):
        t = 255 * np.sum(hist[0][:i])
        liste[i] = t  
    
    neu = np.zeros(img.shape)
    
    for i in range(img.shape[0]): #Row
       for j in range(img.shape[1]): #column
           neu[i,j] = liste[img[i,j]]
    
    
    return neu       

ausgleich1 = histogrammAusgleich(bild1)
histAusgleich1 = np.histogram(ausgleich1,bins=256,range=(0,256))

ausgleich2 = histogrammAusgleich(bild2)      
histAusgleich2 = np.histogram(ausgleich2,bins=256,range=(0,256))

plt.figure(3)
plt.hist(ausgleich1.flatten(),bins=256,range=(0,256))

plt.figure(4)
plt.hist(ausgleich2.flatten(),bins=256,range=(0,256))

plt.figure(5)
plt.imshow(ausgleich1, cmap="gray")

plt.figure(6)
plt.imshow(ausgleich2, cmap="gray")


#Der Kontrast in den Bildern wurde stark verbessert, 
#sodass man deutlich mehr im Bild erkennen kann.
#Die Histogramme decken dementsprechend ein größeres Spektrum ab
#und sind deshalb breiter als vorher. 
  
