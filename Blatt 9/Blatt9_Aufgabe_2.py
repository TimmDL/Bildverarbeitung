# Blatt 9 - Aufgabe 2

import numpy as np
import matplotlib.pyplot as plt

from skimage.filters import gaussian, laplace
from skimage.io import imread
from skimage.util import random_noise

#Aufgabenteil 1
mandrill = imread("mandrill.png")
sig = 3
gausFilter = gaussian(mandrill, sigma=sig)
varianz = 0.01
gausRauschen = random_noise(mandrill, mode='gaussian', var=varianz)

plt.imshow(mandrill,cmap="gray")
plt.imshow(gausFilter,cmap="gray")
plt.imshow(gausRauschen, cmap="gray")


#Aufgabenteil 2

mandrillLaplace = laplace(mandrill)
filterLaplace = laplace(gausFilter)
rauschenLaplace = laplace(gausRauschen)

plt.imshow(mandrillLaplace,cmap="gray")
plt.imshow(filterLaplace,cmap="gray")
plt.imshow(rauschenLaplace, cmap="gray")

#Nur bei dem normalen Gaußfilter (rauschenLaplace) lässt sich der Mandrill noch erkennen
#Das kommt dadurch, dass bei Laplace die Kanntenerkennung mittels dem Übergang
#zwischen positiven und negativen Werten ermittelt wird (Nulldurchgang).
#Beim Gauß Filter werden die Kanten nach dr Anwendung des Laplace Filters sichtbar,
#da das Bild vorher geglätet wurde


#Aufgabenteil 3
sig = 2
rauschenFilter = gaussian(gausRauschen, sigma=sig)
rauschenLaplaceFilter = laplace(rauschenFilter)
plt.imshow(rauschenLaplaceFilter, cmap="gray")

# Durch Anwendung des Gauß Filters auf ein verrauschtes Bild
# lässt sich trotzdem ein gutes Ergebnis bekommen. (sigma = 2)

