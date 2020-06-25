# Blatt 7 - Aufgabe 5

import numpy as np

from skimage.io import imread, imsave, imshow

import skimage.util as util

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