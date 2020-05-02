# Blatt 1 Aufgabe 6

import numpy as np
from skimage.io import imread, imsave

# 1.
img = imread("mandrill.png")

# 2.
min = np.min(img)
print("Min :" + str(min))

max = np.max(img)
print("Max :" + str(max))

ave = np.average(img)
print("Durchschnitt :" + str(ave))

std = np.std(img)
print("Standardabweichung :" + str(std))

# 3. Jeweils die Koodrniaten zum ersten Minimum oder Maximium
minX = np.where(img == np.amin(img))[0][0]
minY = np.where(img == np.amin(img))[1][0]
print("Min X Koordinate: " + str(minX))
print("Min Y Koordinate: " + str(minY))

maxX = np.where(img == np.amax(img))[0][0]
maxY = np.where(img == np.amax(img))[1][0]
print("Max X Koordinate: " + str(maxX))
print("Max Y Koordinate: " + str(maxY))



