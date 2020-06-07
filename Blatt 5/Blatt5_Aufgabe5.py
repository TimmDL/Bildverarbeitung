# Blatt 5 - Aufgabe 5

import numpy as np
import skimage.color

from skimage.io import imread

import matplotlib.pyplot as plt
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

pink1red = pink1[:,:,0]
pink1green = pink1[:,:,1]
pink1blue = pink1[:,:,2]
pink1gray = np.mean([pink1red, pink1blue, pink1blue], axis=0)
pink1graymask = np.min(np.ma.array(pink1gray, pink1maske))
print(pink1graymask)