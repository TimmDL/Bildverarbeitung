# Blatt 8 - Aufgabe 2

import numpy as np
import matplotlib.pyplot as plt

from skimage.filters import sobel, sobel_h, sobel_v
from skimage.io import imread

#Teilaufgabe 1

mandrill = imread("mandrill.png")

mandrillSobel = sobel(mandrill)
plt.imshow(mandrillSobel, cmap="gray") 


