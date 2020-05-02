#Blatt1 Aufgabe 4

import numpy as np
from skimage.io import imread, imsave
import matplotlib.pyplot as plt

img = imread("mandrill.png")
print (img)

#spieglen vertikal
img2 = np.fliplr(img)
plt.imshow(img2, cmap="gray")

#spiegelen horizontal
img3 = np.flipud(img)
plt.imshow(img3, cmap="gray")

#nacheinander spiegeln
img4 = np.flip(img)
plt.imshow(img4, cmap="gray")

#neues größeres Bild
img5 = np.resize(img, (1024,1024))
img5[0:512,0:512] = img
img5[0:512,512:1024] = img2
img5[512:1024,0:512] = img3
img5[512:1024,512:1024] = img4
plt.imshow(img5, cmap= "gray")

#Negativ erstellen
img6 = np.negative(img)
plt.imshow(img6, cmap="gray")

#Nasenspitze erneut
#Lösung: ja es wird die Änderung auch auf das Originalbild angewandt (man siehe den Ort der schwarzen Pixel)
#Range, welche von img7 bearbeitet wird, kann auch erhöht werden, damit es deutlich sichtbarer wird
img7 = img[320:450,120:380]
img7[60:60,120:120] = 0
plt.imshow(img7, cmap="gray")
plt.imshow(img,cmap="gray")

#Maske erstellen
img8 = np.zeros_like(img)
img8[320:450,120:380] = img7
plt.imshow(img8, cmap="gray")
