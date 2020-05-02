#Blatt 1 Aufgabe 3

import numpy as np
from skimage.io import imread, imsave
import matplotlib.pyplot as plt

img = imread("mandrill.png")
print (img)

plt.imshow(img, cmap='gray')

img2 = img[320:450,120:380]
print (img2)
plt.imshow(img2, cmap="gray")
plt.imsave("mandrill_Nase.png", img2, cmap="gray")

img3 = np.copy(img)
img3[250,250] = 0
#print(img3[250,250])
plt.imshow(img3, cmap="gray")

img4 = np.copy(img)
img4[40:90,135:375] = 0
plt.imshow(img4, cmap="gray")

