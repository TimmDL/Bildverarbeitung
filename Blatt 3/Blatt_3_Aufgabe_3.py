# Blatt 3 - Aufgabe 3

import numpy as np

from skimage.io import imread

import matplotlib.pyplot as plt

fehler = imread("mitFehler.png")
original = imread("ohneFehler.png")

# Aufgabenteil 1
dif =  original - fehler 
add = dif + original

plt.imshow(add, cmap="gray")

#Aufgabenteil 2
dif[dif>1] = 1
plt.imshow(dif, cmap="gray")

#Aufgabenteil 3
# a)
coor = np.nonzero(dif)


coor = np.asarray(coor)
print(coor)




def count(arr):
     fehler = 0
     comp_arr = np.full(arr.shape, False, dtype=bool) #initialize
     arr_height = arr.shape[0]
     arr_width = arr.shape[1]

     for i in range(arr_height): #Row
        for j in range(arr_width): #column

            center = arr[i,j]

            #Check edges
            if i == 0: #left side
                left = arr[i,j]
            else:
                left = arr[i-1], j]

            if i == arr_height - 1: #right side
                right = arr[i,j]
            else:
                right = arr[i+1,j]

            if j == 0: #up
                up = arr[i,j]
            else:
                up = arr[i, j-1]

            if j == arr_width - 1: #down
                down = arr[i,j]
            else:
                down = arr[i, j+1]
                
            print(left) 
            
count(coor)
