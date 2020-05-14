# Blatt 2 - Aufgabe 2

import numpy as np

from skimage.io import imread, imsave, imshow

import matplotlib.pyplot as plt
import math as m

def gaus(x):
    n = (1 / np.sqrt(2 * m.pi * np.power(1, 2.))) * np.exp(-np.power(x - 0.2, 2.) / (2 * np.power(1, 2.)))
    return n

i = -5 
index = 0
arr = np.zeros(52)
while i <= 5:
    arr[index] = gaus(i/52)
    i += (1/52)*10
    index += 1
    
arr = np.interp(arr, (arr.min(), arr.max()), (0, 255))

arr = np.round(arr)
    
a = np.empty([100,52])
a = np.array([arr]*100)

plt.imshow(a)


# Bei Veränderung der Standardabweichung (sigma) ändert sich am Bild/ an den Werten nichts
# Bei Erhöhung des Erwartungwerts (mu) verschiebt sich das Bild nach rechts 
# Bei Senkung des Erwartungwerts (mu) verschiebt sich das Bild nach links


    