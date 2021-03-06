# Blatt 7 - Aufgabe 5

import numpy as np

from skimage.io import imread, imsave, imshow

import skimage.util as util
import skimage.filters as filters

import matplotlib.pyplot as plt


# Aufgabenteil 1
einstein = imread("einstein.png")

sigma = 1.3
vari = sigma**2

def gaus(img, varianz):
    result = util.random_noise(img,mode="gaussian",var=varianz)
    return result

gausEinstein = gaus(einstein,vari)

plt.imshow(gausEinstein, cmap="gray")

# Bei einer Standardabweichung von 1.3 lässt sich Einstein noch erkennen,
# bei höheren Sigmawerten nur nich erahnen.
# Der Kragen, die Auggen und der Schnurrbart lassen sich noch relativ gut erkennen.
# Die Gesichtszüge nicht mehr so gut
#

# Aufgabenteil 2
ballon = imread("ballon.png")
plt.imshow(ballon)


# Das Bild zeigt einen Ballon. In der mitte des Bildes ist ein gelber Kreis.
# Um den mittleren Kreis bilden sich mehrere Ringe, wobei sich die verschiedenen 
# Farben spiral-förmig nach außen drehen

sigma2 = 10

def gausFarb(img, sig):
    result = filters.gaussian(img,sigma=sig,multichannel=True)
    return result

gausBallon = gaus(ballon,sigma2)

plt.imshow(gausBallon, cmap="gray")

# Bei sigma = 10 lässt sich die spiralförmige Anordnung der Farben noch erkennen
# Bei sigma = 20 lässt sie sich nur noch erahnen.
# In beiden Fällen lässt sich aber nichts anderes erkennen, außer dass
# im Bild viele verschiedene Farben verwendet werden.
# Umso höher sigma wird, desto weniger gemischte Farben gibt es (sonst nur Rot,gelb,blau)

#Aufgabenteil 3
gletscher = imread("gletscher.png")

 
max1 = 110
max2 = 215
 
def slice(img):
    row = img.shape[0]
    column = img.shape[1]
    sliced = np.zeros((row,column),dtype = 'uint8')
    for i in range(row):
        for j in range(column):
            if img[i,j]>max1 and img[i,j]<=max2:
                sliced[i,j] = 127
            else:
                if img[i,j]>max2:
                    sliced[i,j] = 255 
                else:
                    sliced[i,j] = 0
            
    return sliced      

gletscherSliced = slice(gletscher)
plt.imshow(gletscherSliced, cmap="gray")

# Die Spizen der Berge sind relativ hell, einige Steine auf der rechten Seite 
# sind ebenfalls relativ hell und die Steine im See sind dunkler als der See.

# Dies führt dazu dass einige Bereichne nicht richtig zugeordnet werden können.

   




