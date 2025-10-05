#!/usr/bin/env python3

#While loop Opdracht

#imports
import sys
import os
import time

#Variabelen
total = 0

#Function  
def clr():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def typer(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    
   

typer(".........................OK")

#Vraag om een positief getal in de terminal

typer("Hello, how are you?")
typer("I will ask you a positive number. Please only give positive ones")
time.sleep (2.5)
clr()

#The loop
psoi = int(input("Please give me a positive number: "))
while (psoi > 0):
    
    
    total += psoi
    psoi = int(input("Please give me a positive number: "))
    #Vraag getal via terminal

time.sleep (2)
print(total) 
    


#For i loop opdracht

#Variabeles
latot = 0

#Vraag hoeveel nummers
aantal = int(input("How many numbers do you want?: "))

#for i loop
for i in range (0,10,1):
    
    #vraag getal via terminal
    aantal = int(input("How many numbers do you want?: "))
    latot = latot + aantal
    
print(latot)
