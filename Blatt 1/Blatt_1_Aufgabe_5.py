# Blatt 1 - Aufgabe 5

import numpy as np
from skimage.io import imread, imsave
import matplotlib.pyplot as plt
import time

# a)
def testePixel (img):
    tic = time.time()
    for n in range(img.shape[0]):
        for m in range(img.shape[1]):
            if 99 < img[n,m] < 200:
                pass # do nothing
    toc = time.time()
    diff = toc - tic
    print(diff)             

# b)
    
    
    
img = imread("mandrill.png")
testePixel(img)
