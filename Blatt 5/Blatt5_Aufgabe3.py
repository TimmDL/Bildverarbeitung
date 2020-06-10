# Blatt 5 - Aufgabe 3

import numpy as np

from skimage.io import imread

import matplotlib.pyplot as plt
import math as m

mandrill = imread("mandrillFarbe.png")


#RGB -> CMY
def RGBtoCMY(img):
    neu = np.zeros(img.shape)
    img = img / 255
    for i in range(img.shape[0]): #Row
        for j in range(img.shape[1]): #column
            c = (1.0 - img[i,j,0])
            m = (1.0 - img[i,j,1])
            y = (1.0 - img[i,j,2])
            neu[i,j,0] = c
            neu[i,j,1] = m
            neu[i,j,2] = y
            
    return neu

mandrillCMY = RGBtoCMY(mandrill)


#CMY -> RGB
def CMYtoRGB(img):
    neu = np.zeros(img.shape)
    for i in range(img.shape[0]): #Row
        for j in range(img.shape[1]): #column
            c = (1.0 - img[i,j,0])
            m = (1.0 - img[i,j,1])
            y = (1.0 - img[i,j,2])
            neu[i,j,0] = c
            neu[i,j,1] = m
            neu[i,j,2] = y
            
    return neu      

mandrillRGB = CMYtoRGB(mandrillCMY)    

#plt.imshow(mandrillRGB)

#RGB -> HSI
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
                
               neu[n,o,0] = h / 360
               neu[n,o,1] = s
               neu[n,o,2] = i
              
       return neu
   
mandrillHSI = RGBtoHSI(mandrill)  
plt.imshow(mandrillHSI) 

#HSI -> RGB
def HSItoRGB(img):
    neu = np.zeros(img.shape)
    for n in range(img.shape[0]): #Row
           for o in range(img.shape[1]): #column 
               h = img[n,o,0] * 360
               s = img[n,o,1]
               if(s>1):
                   s=1    
               i = img[n,o,2]
               if(i>1):
                   i=1
               if(s==0):
                   r=g=b=i
               else:
               
                   if(0 <= h <= 120):
                       b = (1/3) * (1 - s)
                       r = (1/3) * ( 1 + ((s * m.cos(np.radians(h))) / (m.cos(np.radians(60 - h)))))
                       g = 1 - (r + b)

                   if(120 < h <= 240):
                       h = h - 120
                       r = (1/3) * (1 - s)
                       g = (1/3) * ( 1 + ((s * m.cos(np.radians(h))) / (m.cos(np.radians(60 - h)))))
                       b = 1 - (r + g)

                   if(240 < h <= 360):
                       h = h - 240
                       g = (1/3) * (1 - s)
                       b = (1/3) * ( 1 + ((s * m.cos(np.radians(h))) / (m.cos(np.radians(60 - h)))))
                       r = 1 - (g + b)    
        
               
               neu[n,o,0] = r*i*3
               neu[n,o,1] = g*i*3
               neu[n,o,2] = b*i*3
               
               
    return neu       
    
mandrillRGB2 = HSItoRGB(mandrillHSI)  
plt.imshow(mandrillRGB2)  

