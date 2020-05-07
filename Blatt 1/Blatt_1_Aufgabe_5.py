# Blatt 1 - Aufgabe 5

import numpy as np

from skimage.io import imread, imsave

import time

# 1)

def testePixelLoop (img):

    for n in range(img.shape[0]):

        for m in range(img.shape[1]):

            if 99 < img[n,m] < 200:

                pass # do nothing
# 2)

def testePixelBroadcast (img):
 for imgsum in np.nditer(img):
        if 99 < imgsum < 200:
            pass

# 3)

img = imread("mandrill.png")


# 100 Aufrufe der Schleifen Funktion

tic = time.time()

i = 0

while i < 100:

    testePixelLoop(img) 

    i += 1

toc = time.time()

diffLoop = toc - tic

print("Rechendauer mit Schleife: " +  str(diffLoop))  

    

# 100 Aufrufe der Broadcast Funktion
# Wir hatten Probleme die Aufgabenstellung richtig zu verstehen, da wir nicht genau wussten,
# wie genau das ohne Schleife funktionieren soll. WIr haben versucht uns online schlau zu machen, aber
# selbst dort ist immer auch eine Schleife in Verbindung mit Broadcasting zu finden, deswegen haben wir 
# jetzt diese Lösung mit dem np.nditer Ansatz für am sinnvollsten gehalten

tic = time.time()

i = 0

while i < 100:

    testePixelBroadcast(img) 

    i += 1

toc = time.time()

diffBroad = toc - tic

print("Rechendauer mit Broadcasting: " +  str(diffBroad))



print("Differenz: " + str(diffLoop - diffBroad))

