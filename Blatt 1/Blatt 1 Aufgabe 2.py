#Aufgabe 2 Blatt 1

import numpy as np
from skimage.io import imread, imsave
u = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
v = [0,1,2,3,4,5,6,7,8,9,10,11]
m = np.array([v])
m.shape = (4,3)

produkt = m * 1.2

print(produkt.astype(int))
print(produkt * 1.2)

print(produkt.dtype)

hadamart = np.multiply(produkt,produkt)

print(hadamart)






