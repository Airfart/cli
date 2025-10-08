#!/usr/bin/env python3

#In deze opdracht moeten wij Array, for-loop, while-loop, if-elif-else gebruiken
#Voor opdracht zie afbeelding opdracht 9

# -- opdracht 1 -- 
# -- 1. maak een lijst [arrays], genaamd fruit, met 6 verschilende soorten fruit
# -- 2. gebruik een for-loop om alle soorten fruit een voor een te printen

#Imports
import sys
import time
import os

#Arrays -- opdracht 1
fruit = ["mango", "appel", "banaan", "kiwi", "ananas", "druif"]

#explaining --opdracht 1
print("printing all the fruits from the list")
time.sleep(2)
#for-loop --opdracht 1
for i in range(len(fruit)):
    print(fruit[i])
    time.sleep(1.5)
#Dit is het einde van opdracht 1. Over naar opdracht 2
#Asking the user for the hour of the local time
print("Please give me a time in hours.")
time.sleep (2)
print("You can choose between 0-23")
time.sleep (2)
    
while True:
    try:
        uur = int(input("Wat is het huidige uur? (0-23): "))

        if 0 <= uur <= 11:
            print("Het is ochtend")
        elif 12 <= uur <= 17:
            print("Het is middag")
        elif 18 <= uur <= 23:
            print("Het is avond")
        else:
            print("Je hebt een ongeldige uur ingevuld!")
            #break  # stop de loop bij ongeldige invoer
    except ValueError:
        print("Ongeldige invoer! Vul een getal in.")
