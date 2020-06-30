# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:03:03 2020

@author: Jan Harder
"""

from random import randrange
import operator



def randomRiddle():
    
    operators = {0: operator.add,
             1: operator.sub,
             2: operator.mul,
             3: operator.pow}
    
    operator1,number1 = newOperator()
    operator2,number2 = newOperator()
    operator3,number3 = newOperator()
    
    operatorList = [operator1,operator2,operator3]
    numberList = [number1,number2,number3]
    
    seq = list(range(6))
    seq[0] = randrange(10)
    
    for i in range(1,5):
        oper = operatorList[i%3]
        prev = seq[i-1]
        number = numberList[i%3]
        seq[i] = operators[oper](prev, number)
        
    print(seq)     
    print(operatorList)
    print(numberList)
    
def newOperator():
    operator = randrange(4)
    if (operator == 3):
        number = randrange(4)
    else:
        number = randrange(7)
    return operator,number
    


def add(number,prev):
    return prev + number

def sub(number, prev):
    return prev - number

def multipy(number, prev):
    return 


        
    
