# Blatt 8 - Aufgabe 4

import numpy as np
import matplotlib.pyplot as plt

from skimage.filters import sobel
from skimage.io import imread


# Aufgabenteil 1

##########################################################
#Bild aus aus Aufgabe 4
opera = imread("opera.png")
blue = np.zeros(opera.shape[0:2])
for i in range(blue.shape[0]): #Row
    for j in range(blue.shape[1]): #column
        # Gelb [R=255,G=255,B=0] ist das Gegemteil im RGB Raum von reinem Blau
        v = opera[i,j,2] - 0.5*opera[i,j,0] - 0.5*opera[i,j,1]
        blue[i,j] = v
plt.imshow(opera)
operaBlueSobel = sobel(blue)
##########################################################


operaDegree = np.arctan(operaBlueSobel)
plt.imshow(operaDegree)

for i in range(operaDegree.shape[0]): #Row
    for j in range(operaDegree.shape[1]): #column
        v = operaDegree[i,j]
        if (-22.5<=v and v<22.5):
            operaDegree[i,j] = 0
        else:
            if (22.5<=v and v<67.5):
                operaDegree[i,j] = 45
            else:
                if (-67.5<=v and v<-22.5):
                    operaDegree[i,j] = -45
                else:
                    operaDegree[i,j] = 90
                    
plt.imshow(operaDegree, cmap="gray")                    
                    
                
                



