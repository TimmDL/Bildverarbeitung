# Blatt 2 - Aufgabe 5

import numpy as np

from skimage.io import imread, imsave, imshow

import matplotlib.pyplot as plt
import math as m

img = imread("mandrill.png")

sigma = 100

def addGauss(img, simga):
      erwartungswert = 0
      g = np.random.normal(erwartungswert, sigma,(img.shape))
      g = g.reshape(img.shape)
      gausImg = img + g
      return gausImg

gaus = addGauss(img, sigma)  
gaus = np.interp(gaus, (gaus.min(), gaus.max()), (0, 255))   
    
 
  
    
def addSaP(img, veraenderung):
    Kopie = np.copy(img)
      
    s = np.ceil(img.size * 0.5 * veraenderung)
    coords = [np.random.randint(0, i - 1, int(s))
              for i in img.shape]
    Kopie[coords] = 255 

    p = np.ceil(img.size * 0.5 * veraenderung)
    coords = [np.random.randint(0, i - 1, int(p))
              for i in img.shape]
    Kopie[coords] = 0
    
    return Kopie

sap = addSaP(gaus, 0.1)
sap = np.interp(sap, (sap.min(), sap.max()), (0, 255))

plt.imshow(sap) 


# Umso höher der Wet "veraenderung" ist, desto mehr Störungen/ Noise in Form von
# schwarzen und weißen Störungen (Salt and peper) gibt es auf dem bild

# Umso höher Sigma/die standarbabweichung ist, desto weniger erkennt man im Bild, 
#da die Farben sich immer weiter annähern