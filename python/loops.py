#!/usr/bin/env python3

#imports
import sys
import os
import time

#Variabelen
total = 0


#Function clear text
def clr():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


#Function telepromter text typer
def typer(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()   

typer(".........................OK")


# - While loop Opdracht - 

#Vraag om een positief getal in de terminal

typer("Hello, how are you?")
typer("I will ask you a positive number. Please only give positive ones")
time.sleep (2.5)
clr()

# - The loop -
# psoi ? RCS: WTF is dat voor een naam voor een Variabele?
# YMW: Positive getal

typer("The Loop -") # for debugging purpose
psoi = int(input("Please give me a positive number: "))
while (psoi > 0):
    
    total += psoi
    psoi = int(input("Please give me a positive number: "))
    #Vraag getal via terminal

time.sleep (2)
print(total) 
    

# - For i loop opdracht -

typer("The For -") # for debugging purpose
time.sleep(1.5)

#Vraag hoeveel nummers
aantal = int(input("How many numbers do you want?: "))

#Variabeles
totaal = 0

#for i loop BEGINT
for i in range(0,10,1):
    
    #vraag getal via terminal
    aantal = int(input("How many numbers do you want?: "))
    totaal = totaal + aantal
    
print(totaal) # Functie lijkt zich te herhalen. Wanneer is deze klaar ... BREAK?
