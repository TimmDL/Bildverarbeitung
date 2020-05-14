# Blatt 2 - Aufgabe 1

import numpy as np

from skimage.io import imread, imsave, imshow

import matplotlib.pyplot as plt

def calcNDVI (red, nir):
    red = red.astype(np.float)
    nir = nir.astype(np.float)
    ndvi = (nir - red) / (nir + red)
    print(np.shape(ndvi))
    print(ndvi)
    plt.imshow(ndvi)

red = imread("band3.png")
nir = imread("band4.png")

calcNDVI(red, nir)

# "Dieser Index gibt Werte zwischen -1,0 und 1,0 aus, die hauptsächlich Grünanteile darstellen.
# Die negativen Werte werden hauptsächlich durch Wolken, Wasser und Schnee verursacht, die Werte um Null
# von Stein und nackter Erde. Sehr niedrige NDVI-Werte (0,1 und niedriger) entsprechen 
#unwirtlichen Flächen mit steiniger oder sandiger Oberfläche oder Schnee. Mäßige Werte 
#(0,2 bis 0,3) entsprechen Strauch- und Grasflächen, während hohe Werte (0,6 bis 0,8) 
#gemäßigten und tropischen Regenwäldern entsprechen." (https://desktop.arcgis.com/)
#
#
# Band 3 entspricht der Wellenlänge von rotem Licht 
# und Band 4 entspricht der Wellenlänge von NIR.


# Die grünen Punkte (Werte ab 0.5) stellen Grasflächen bis hinzu Bäumen dar.
# Die Abstufungen der Graustufen bilden die Intensität ab.



             
