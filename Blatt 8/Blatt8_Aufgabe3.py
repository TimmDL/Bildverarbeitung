# Blatt 8 - Aufgabe 4

import numpy as np
import matplotlib.pyplot as plt

from skimage.filters import sobel
from skimage.io import imread
from skimage.color import rgb2gray

#Aufgabenteil 1
opera = imread("opera.png")
operaGray = rgb2gray(opera)
operaGraySobel = sobel(operaGray)
#plt.imshow(operaGraySobel, cmap="gray")

# Nahezu alle Kanten werden gefunden. Besonders stark sind die Kanten,
# die an den Himmel grenzen. Die Spiegelungen des Wassers in den Fenstern führen
# zu fäschlich erkannten Kanten.

#Aufgabenteil 2
blue = np.zeros(opera.shape[0:2])
for i in range(blue.shape[0]): #Row
    for j in range(blue.shape[1]): #column
        # Gelb [R=255,G=255,B=0] ist das Gegemteil im RGB Raum von reinem Blau
        v = opera[i,j,2] - 0.5*opera[i,j,0] - 0.5*opera[i,j,1]
        blue[i,j] = v
           
#Aufgabenteil 3 
operaBlueSobel = sobel(blue)
plt.imshow(operaBlueSobel,cmap="gray")    

# Im neuen Ergebnis werden die Kanten zwischen Himmel und Opernhaus deutlich
# stärker herausgehoben. Die anderen (inneren) Kanten werden nur schwach angedeutet

            