#!/usr/bin/env python3

import time
import os
import sys

#function
def clr():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

#Zeg hallo
print ("Hello")
time.sleep (2)

#input leeftijd
max = 18
age = int(input("Wat is je leeftijd: "))
clr()
print ("Very cool in 20 years you will be",age + 20)
time.sleep (3)

#If-Else 
if age > max:
    print ("You are old enough")
    
else: 
    print("you are too young")

