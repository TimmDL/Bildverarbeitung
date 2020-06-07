# Blatt 5 - Aufgabe 4

import numpy as np

from skimage.io import imread

import matplotlib.pyplot as plt
import math as m

# 1.
mandrill = imread("mandrillFarbe.png")
plt.imshow(mandrill)

# 2.
def invert(img):
    img =  256 - img
    return img

# Für jeden Pixelwert wird die jeweils gegeteilige Farbe berechnet. z.B Schwarz wird zu weiß 
# und rot wird zu blau.

mandrillInvert = invert(mandrill)
plt.imshow(mandrillInvert)

# 3. 
#Je heller ein Bereich in einem der Graustufenbilder ist,
# desto intensiver ist dort die jeweilige Farbe im Originalbild
rot = mandrill[:,:,0]
gruen = mandrill[:,:,1]
blau = mandrill[:,:,2]
plt.imshow(rot, cmap = "gray")
plt.imshow(gruen, cmap = "gray")
plt.imshow(blau, cmap = "gray")

# 4. (b,g,r)
add = np.dstack((blau,gruen,rot))
plt.imshow(add)
# Wie und wieso ändert sich das Bild?
# Die roten Bereiche werden blau gefärbt, da jetzt der B-Wert in diesen Bereich hoch ist anstatt dem R-Wert
# Die leicht blauen Bereiche werden leicht rot gefärbt, da jetzt der R-Wert in diesen bereich hoch ist anstatt der B-Wert.
# Da jetzt bei der additiven Farbmischung jeweils der Rot und Blau Wert vertauscht werden,
# ändern sich nicht nur die roten und blauen Bereiche.

# 5.
grau = np.mean([rot, blau, gruen], axis=0)
print(grau)
plt.imshow(grau, cmap = "gray")
