# Blatt 1 - Aufgabe 5

import numpy as np
from skimage.io import imread, imsave
import matplotlib.pyplot as plt
import time

# 1)
def testePixelLoop (img):
    for n in range(img.shape[0]):
        for m in range(img.shape[1]):
            if 99 < img[n,m] < 200:
                pass # do nothing
          

# 2)
 #  def testePixelBroadcast (img):
       

# 3)
img = imread("mandrill.png")
    
# 100 Aufrufe der Schleifen Funktion
tic = time.time()
i = 0
while i < 10:
    testePixelLoop(img) 
    i += 1
toc = time.time()
diffLoop = toc - tic
print("Rechendauer mit Schleife: " +  str(diffLoop))  
    
# 100 Aufrufe der Broadcast Funktion
tic = time.time()
i = 0
   ## while i < 100:
   ##   i += 1

#testePixelBroadcast(img) 
toc = time.time()
diffBroad = toc - tic
print("Rechendauer mit Broadcasting: " +  str(diffBroad))

print("Differenz: " + str(diffLoop - diffBroad))


       
    
    
