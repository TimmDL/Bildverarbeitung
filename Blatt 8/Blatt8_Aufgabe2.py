# Blatt 8 - Aufgabe 2

import numpy as np
import matplotlib.pyplot as plt

from skimage.filters import sobel, sobel_h, sobel_v, gaussian
from skimage.io import imread
import math as m

#Teilaufgabe 1

mandrill = imread("mandrill.png")

mandrillSobel = sobel(mandrill)
#plt.imshow(mandrillSobel, cmap="gray") 



def kantenBild(img,grenzwert):
    kanten = np.zeros(img.shape)
    for i in range(img.shape[0]): #Row
       for j in range(img.shape[0]): #column
            if (img[i,j]>grenzwert):
                kanten[i,j] = 1
            else:
                kanten[i,j] = 0
    return kanten            
                

#plt.imshow(kantenBild(mandrillSobel,0.1), cmap="gray") 

# ja,die wichtigsten Kanten wie z.B. sinf gefunden worden. Zusätlich wurden im Fell
# viele Kanten gefunden. 
# Ein Grenzwert von 0.1 sind die Kanten am besten zu erkennen.


#Aufgabenteil 2
sig = 2.3
mandrillGauss = gaussian(mandrill,sigma=sig)

mandrillGaussSobel = sobel(mandrillGauss)
mandrillGaussSobelKanten = kantenBild(mandrillGaussSobel,0.05)
#plt.imshow(mandrillGaussSobelKanten, cmap="gray") 

# Je größer das Sigma desto mehr wird das Bild geglättet wodurch immmer weniger Kanten erkannt werden.
# Bei sehr hohem Sigma wird das Bild deshalb Schwarz
# Das beste Ergebnis ist bei sigma = 2.3. Bei diesem Wert werden weniger Kanten im Fell erkannt, aber noch die wichtigen
# im Gesicht

#Aufgabenteil 3

original150 = mandrill[150,:]
gauss150 = gaussian(mandrill,sigma=sig)[150,:]
gaussHoch150 = gaussian(mandrill,sigma=sig*3)[150,:]

originalSobelV = sobel_v(mandrill)
gaussSobelV = sobel_v(gaussian(mandrill,sigma=sig))
gaussHochV = sobel_v(gaussian(mandrill,sigma=sig*3))

originalSobelV150 = originalSobelV[150,:]
gaussSobelV150 = gaussSobelV[150,:]
gaussHochV150 = gaussHochV[150,:]

# plt.figure(1)
# plt.plot(original150,originalSobelV150)
# plt.figure(2)
# plt.plot(gauss150,gaussSobelV150)
# plt.figure(3)
# plt.plot(gaussHoch150,gaussHochV150)

# Die Kurven werden von Figure zu Figure glatter bzw. runder und es werden weniger Kurven.


# Aufgabenteil 4
gradMandrill = np.arctan(mandrill)
gradVerbesserung = np.arctan(mandrillGaussSobelKanten)

hist1 = np.histogram(gradMandrill,bins=9,range=(0,256))
plt.figure(1)
plt.hist(gradMandrill,bins=9,range=(0,256))

hist2 = np.histogram(gradVerbesserung,bins=9,range=(0,1))
plt.figure(2)
plt.hist(gradVerbesserung,bins=9,range=(0,1))

# In Figure 2 gibt es zwei Bereiche mit Werten im Histogram, in figure 1 nur einen 

hist3 = np.histogram(gradMandrill,bins=9,range=(0,256), weights=sobel(mandrill))
plt.figure(3)
plt.hist(gradMandrill,bins=9,range=(0,256),weights=sobel(mandrill))

hist4 = np.histogram(gradVerbesserung,bins=9,range=(0,1),weights=sobel(mandrillGaussSobelKanten))
plt.figure(4)
plt.hist(gradVerbesserung,bins=9,range=(0,1),weights=sobel(mandrillGaussSobelKanten))

# Von Figure 1 zu Figure 3 ändert es sich dahingehend dass das Histogramm nicht mehr so 
#gleichmäßig aussieht und es innerhalb des Balkens zwei Peaks gibt.

# Von Figure 2 zu Figure 4 ändert es sich dahingehend dass der erste bereich mit Werten deutlich kleiner 
# wird und der zweite Bereich deutlich größer wird. Der höchste Peak ist nun in rechten bereich




                



