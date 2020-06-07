# Blatt 5 - Aufgabe 4

import numpy as np
import skimage.color

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

# 6. 
# intensiät = 1
hsv1 = skimage.color.rgb2hsv(mandrill)
hsv1[:,:,1] = 1
rgb1 = skimage.color.hsv2rgb(hsv1)
plt.imshow(rgb1)
# Bei 100% Sättigung sind die Farben sehr kräftig und klar, da 100% gesättigte Farben kein weiß enthalten. 

# intensiät = 0
hsv0 = skimage.color.rgb2hsv(mandrill)
hsv0[:,:,1] = 0
rgb0 = skimage.color.hsv2rgb(hsv0)
plt.imshow(rgb0)
# Bei 0% Sättigung gibt es gar keine Farben und das Bild wird in Grautönen angezeigt.

#7.

# +60 Grad
hsv60 = skimage.color.rgb2hsv(mandrill)
hsv60[:,:,0] = ((hsv60[:,:,0] + 60/360) % 1)
rgb60 = skimage.color.hsv2rgb(hsv60)
plt.imshow(rgb60)

# Da die Werte auf 0 bis 1 skalliert sind, darf nur ein Wert unter 1 addiert werden (60/360) und es
# muss Modulo 1 geserechnet werden, da 1 das Maximum ist.
# Die neuen Farben lassen sich anhand der Hue Scale für RGB errechnen (https://en.wikipedia.org/wiki/File:HueScale.svg)
# So wird zum Beispiel, das helle blau (ca. 200) zu lila (ca. 260)

# +120 Grad
hsv120 = skimage.color.rgb2hsv(mandrill)
hsv120[:,:,0] = ((hsv120[:,:,0] + 120/360) % 1)
rgb120 = skimage.color.hsv2rgb(hsv120)
plt.imshow(rgb120)
#Die Nase ändert ihre Farbe von rot(0) zu grün(0+120=120).
#Der blaue(200) Bereich wird pink(200+120=320)




# +240 Grad
hsv240 = skimage.color.rgb2hsv(mandrill)
hsv240[:,:,0] = ((hsv240[:,:,0] + 240/360) % 1)
rgb240 = skimage.color.hsv2rgb(hsv240)
plt.imshow(rgb240)
# Die Nase ändert ihre Farbe von rot(0) zu blau (0+240=240).
#Der Bereich neben der Nase wechselt von blau(200) zu hellgrün((200+240) % 360 = 80)