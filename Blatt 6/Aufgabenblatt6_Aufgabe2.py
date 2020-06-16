# Blatt 6 - Aufgabe 2

import numpy as np
import time

from skimage.io import imread

# Teilaufgabe 1
def varianz(img):
   counter = 0 
   summe = 0
   for i in range(img.shape[0]): #Row
       for j in range(img.shape[1]): #column
           summe += img[i,j]
           counter += 1
   mean = summe / counter
   #print("mean: " + str(mean))
   
   summeVar = 0
   for i in range(img.shape[0]): #Row
       for j in range(img.shape[1]): #column
           summeVar += (img[i,j] - mean) ** 2
   
   var = (1/(img.shape[0]*img.shape[1])) * summeVar
   #print("var: " + str(var))
   
   return (mean,var)

mandrill = imread("mandrill.png")
#varianz(mandrill)

# Aufgabenteil2
def varianz2(img):
   counter = 0 
   summe = 0
   summeVar = 0
   for i in range(img.shape[0]): #Row
       for j in range(img.shape[1]): #column
           summe += img[i,j]
           counter += 1
           summeVar += int(img[i,j]) ** 2
           
   mean = summe / counter
   var = (1/(img.shape[0]*img.shape[1])) * summeVar - mean ** 2
   
   
   #print("mean2: " + str(mean))
   #print("var2: " + str(var))
   return (mean,var)
   
#varianz2(mandrill)


# Aufgabenteil 3
def zeit(img):
    tic1 = time.time()
    for x in range(1,11):
        varianz(img)
    toc1 = time.time() 
    time1 = toc1-tic1  
    
    tic2 = time.time()
    for x in range(1,11):
        varianz2(img)
    toc2 = time.time() 
    time2 = toc2-tic2 
    
    tic3 = time.time()
    for x in range(1,11):
        np.var(img)
        np.mean(img)
    toc3 = time.time() 
    time3 = toc3-tic3 
    
    print("Zwei For Schleifen: " +str(time1))
    print("Eine For Schleife: " +str(time2))
    print("Referenz: np.var und np.mean: " +str(time3))
    
zeit(mandrill)  

# Die Variante mit zwei doppelten For-Schleifen dauert deutlich länger als die mit einer doppelten
# Forschleife, da diese nur einmal statt zweimal ausgeführt werden muss.

#  Da in der ersten Variante in jedem Durchlauf der Forschleife subtrahiert wird und in der zweiten 
#  Variante nur ein Mal am Ende, wird in der ersten variante öfters gerundet, wodurch das Ergebnis leicht abweicht.
    
    
    
    
        

