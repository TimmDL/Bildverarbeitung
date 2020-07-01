# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:03:03 2020

@author: Jan Harder
"""

from random import randrange
import operator

seq = list(range(7)) #init Zahlenfolge
operatorList = list(range(3)) #init Liste für Operanden
numberList = list(range(3)) #init List für Werte zum addieren/multiplizieren usw.

def randomRiddle():
    
    #Die Zahlen können addiert, subtrahiert, multipliziert oder potenziert werden
    operators = {0: operator.add,
             1: operator.sub,
             2: operator.mul,
             3: operator.pow}
    
    # Operationen bestimmen (können doppelt vorkommen)
    operator1,number1 = newOperator()
    operator2,number2 = newOperator()
    operator3,number3 = newOperator()
    
    operatorList = [operator1,operator2,operator3]
    numberList = [number1,number2,number3]
    
    #Erste Zahl bestimmen(Soll nicht zu groß sein, 
    #damit nicht mit zu großen Zahlen gerechnet werden muss)
    seq[0] = randrange(10)
    
    #Alle restlichen Zahlen bestimmen
    for i in range(1,5):
        oper = operatorList[(i-1)%3]
        prev = seq[i-1]
        number = numberList[(i-1)%3]
        seq[i] = operators[oper](prev, number)
        
    print("Zahlenfolge : " + str(seq[0:6]))
    print("Welche Zahl ist die nächste?")
    
    
    
# Zu fällig eine Zahl von 0-3 fürs Amppen der Rechenoperationen bestimmen 
def newOperator():
    operator = randrange(4)
    if (operator == 3):
        number = randrange(4)
    else:
        number = randrange(7)
    return operator,number

randomRiddle()

# Interface mit begrenzter Anzahl an versuchen
for i in range(1,7):
    if int(input("gesuchte Zahl?"))==seq[6]:
        print("Richtig!!!")
    else:
        print("Leider falsch...versuche es noch einmal!")    
        
print("Keine Versuche mehr übrig")     
print("Die gesuchte Zahl ist: " + str(seq[6]))    

    


        
    
