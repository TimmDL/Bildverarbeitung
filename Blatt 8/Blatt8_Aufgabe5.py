# Blatt 8 - Aufgabe 4

import numpy as np
import matplotlib.pyplot as plt

from skimage.filters import sobel
from skimage.io import imread


# Aufgabenteil 1

##########################################################
#Bild aus aus Aufgabe 4
opera = imread("opera.png")
blue = np.zeros(opera.shape[0:2])
for i in range(blue.shape[0]): #Row
    for j in range(blue.shape[1]): #column
        # Gelb [R=255,G=255,B=0] ist das Gegemteil im RGB Raum von reinem Blau
        v = opera[i,j,2] - 0.5*opera[i,j,0] - 0.5*opera[i,j,1]
        blue[i,j] = v
plt.imshow(opera)
operaBlueSobel = sobel(blue)
plt.imshow(operaBlueSobel,cmap="gray")
##########################################################


operaDegree = np.degrees(np.arctan(operaBlueSobel))
#plt.imshow(operaDegree, cmap="gray")

for i in range(operaDegree.shape[0]): #Row
    for j in range(operaDegree.shape[1]): #column
        v = operaDegree[i,j]
        if (-22.5<=v and v<22.5):
            operaDegree[i,j] = 0
        else:
            if (22.5<=v and v<67.5):
                operaDegree[i,j] = 45
            else:
                if (-67.5<=v and v<-22.5):
                    operaDegree[i,j] = -45
                else:
                    operaDegree[i,j] = 90
                    
plt.imshow(operaDegree, cmap="gray")     

result = np.zeros(operaBlueSobel.shape)                   
                    
 
# Aufgabenteil 2               
for i in range(1,operaDegree.shape[0]-1): #Row
    for j in range(1,operaDegree.shape[1]-1): #column
        degree = operaDegree[i,j] 
        neigbor1=0
        neigbor2=0
        if degree==0:
            neigbor1=operaDegree[i-1,j]
            neigbor2=operaDegree[i+1,j]
        elif degree==45:
            neigbor1=operaDegree[i-1,j-1]
            neigbor2=operaDegree[i+1,j+1]
        elif degree==90:
              neigbor1=operaDegree[i,j-1]
              neigbor2=operaDegree[i,j+1]
        else:
            
             neigbor2=operaDegree[i+1,j-1]
             neigbor2=operaDegree[i-1,j+1]

# Aufgabenteil 3         
        if (degree>=neigbor1 and degree>=neigbor2):
            result[i,j] = degree
            
plt.imshow(result,cmap="gray")            
 
#Aufagbenteil 4           
for i in range(result.shape[0]): #Row
    for j in range(result.shape[1]): #column
        if result[i,j]<90:
            result[i,j]=0

plt.imshow(result,cmap="gray")            
                 
                    
                    
                
            



