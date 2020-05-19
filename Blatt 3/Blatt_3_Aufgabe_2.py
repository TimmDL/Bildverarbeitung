# Blatt 3 - Aufgabe 2

import numpy as np

from skimage.io import imread, imsave, imshow

import matplotlib.pyplot as plt

img1 = imread("bild1.png")
img2 = imread("bild2.png")
img3 = imread("bild3.png")
img4 = imread("bild4.png")
img5 = imread("bild5.png")

# Aufgabenteil 1

add = np.array(img1) + np.array(img2) + np.array(img3) + np.array(img4) + np.array(img5)
add = np.divide(add, 5)
plt.imshow(add, cmap = "gray") 


# Aufgabenteil 2
add2 = np.average( np.array([np.array(img1), np.array(img2), np.array(img3), np.array(img4), np.array(img5)]), axis=0)
plt.imshow(add2, cmap = "gray") 


# Aufgabenteil 3
schwellenwert = 25

def differenz (img, add2):
    dif = img - add2
    dif2 = np.where( dif > schwellenwert, img, dif)
    return dif2  

ver1 = differenz(img1, add2)
ver2 = differenz(img2, add2)
ver3 = differenz(img3, add2)
ver4 = differenz(img4, add2)
ver5 = differenz(img5, add2)

plt.imshow(ver3, cmap = "gray") 

# Aufgabenteil 4
neu = add2 + ver1
plt.imshow(neu, cmap = "gray")

neu2 = add2 + ver2
plt.imshow(neu2, cmap = "gray")

neu3 = add2 + ver3
plt.imshow(neu3, cmap = "gray")

neu4 = add2 + ver4
plt.imshow(neu4, cmap = "gray")

neu5 = add2 + ver5
plt.imshow(neu5, cmap = "gray")


# Aufgabenteil 5
#ergebniss = neu + neu2 + neu3 + neu4 + neu5
ergebniss =  ver1 + ver2 + ver3 + ver4 + ver5 + add2

ergebniss = np.interp(ergebniss, (ergebniss.min(), ergebniss.max()), (0, 250))




plt.imshow(ergebniss, cmap = "gray")

