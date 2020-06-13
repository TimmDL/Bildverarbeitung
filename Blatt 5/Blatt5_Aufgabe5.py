# Blatt 5 - Aufgabe 5

import numpy as np
import skimage.color

from skimage.io import imread

import matplotlib.pyplot as plt
import numpy.ma as ma
import math as m

# 1. 
pink1 = imread("image_02881.jpg")
pink2 = imread("image_02890.jpg")
gelb1 = imread("image_04650.jpg")
gelb2 = imread("image_04666.jpg")
pink1maske = imread("image_02881_maske.png") - 1
pink2maske = imread("image_02890_maske.png") - 1
gelb1maske = imread("image_04650_maske.png") - 1
gelb2maske = imread("image_04666_maske.png") -1 

def grayScale(img):
    red = pink1[:,:,0]
    green = pink1[:,:,1]
    blue = pink1[:,:,2]
    gray = np.mean([red, green, blue], axis=0)
    return gray

#Grauwertbilder
pink1gray=grayScale(pink1)
pink2gray=grayScale(pink2)
gelb1gray=grayScale(gelb1)
gelb2gray=grayScale(gelb2)

plt.imshow(pink1gray, cmap="gray")


def mittelwert(img,maske):
   counter = 0 
   summe = 0
   for i in range(img.shape[0]): #Row
       for j in range(img.shape[0]): #column
            if (maske[i,j]==255):
                summe += img[i,j]
                counter += 1
   mittelwert = summe / counter                         
   print(mittelwert)

#Mittelwerte
pink1mittel = mittelwert(pink1gray,pink1maske) #109.87
pink2mittel = mittelwert(pink2gray,pink2maske) #109.19
gelb1mittel = mittelwert(gelb1gray,gelb1maske) #121.37
gelb2mittel = mittelwert(gelb2gray,gelb2maske) #122.31


#RGB -> HSI #Funktion aus Aufgabe 3
def RGBtoHSI(img):
       neu = np.zeros(img.shape)
       img = img / 255
       for n in range(img.shape[0]): #Row
           for o in range(img.shape[1]): #column 
               r = img[n,o,0]
               g = img[n,o,1]
               b = img[n,o,2]
               zetaRad = m.acos( (1/2 * ((r-g)+(r-b)) / (m.sqrt((r-g)**2 +(r-b) * (g-b)) + 0.001)))
               zeta = np.degrees(zetaRad)
               
               i = ((1/3) * (r + g + b))
               
               if (r==0 and g==0 and b==0):
                   s = 0
               else:
                   s = 1 - ( 3/(r + g + b)) * min(r,g,b)
               
               if(b <= g):
                   h = zeta
               else:
                   h = 360 - zeta
                
               neu[n,o,0] = h
               neu[n,o,1] = s
               neu[n,o,2] = i
              
       return neu
   
# 2.    
def mittelwertFarbton(img,maske):
   hsi = RGBtoHSI(img)
   hue = hsi[:,:,0]
   counter = 0 
   summe = 0
   
   for i in range(hue.shape[0]): #Row
       for j in range(hue.shape[0]): #column
            if (maske[i,j]==255):
                summe += hue[i,j]
                counter += 1
   mittelwert = summe / counter                         
   print(mittelwert) 

# Mittelwerte Farbtöne
pink1mittelFarbton = mittelwertFarbton(pink1,pink1maske) #148.59
pink2mittelFarbton = mittelwertFarbton(pink2,pink2maske) #155.59
gelb1mittelFarbton = mittelwertFarbton(gelb1,gelb1maske) #80.62
gelb2mittelFarbton = mittelwertFarbton(gelb2,gelb2maske) #87.75


# 3.
"""
 Die Unterschiede zwischen den gleichen Blumenarten sind bei der Methode mit den
 Graustufenbildern deutlich kleiner. Daher eignet sich der Mittelwert der Graustufenbilder besser.
 Das liegt daran, dass bei der Methode über den Farbton (H-Wert) die Sättigung und Intensität 
 vernachlässigt werden. So gehen Informationen verloren. Bei der Methode über den Grauwert werden alle
 zu Verfügung stehenden Informationen verwendet.
"""
