#!/usr/bin/env python3

# Opdracht CS leerjaar 1 - Opdracht 9
#
# Status: Onbekend (Ingeleverd?)
#
# Omschrijving: In deze opdracht moeten wij Array, for-loop, while-loop, if-elif-else gebruiken
# Bijlage: zie afbeelding opdracht-9.png


# -- Imports voor opdracht 1 en 2
import sys
import time
import os


# -- opdracht 1 --
# -- 1.1 maak een lijst [arrays], genaamd fruit, met 6 verschilende soorten fruit
# -- 1.2 gebruik een for-loop om alle soorten fruit een voor een te printen

#Arrays -- opdracht 1.1
fruit = ["mango", "appel", "banaan", "kiwi", "ananas", "druif"]

#explaining --opdracht 1.2
print("printing all the fruits from the list")
time.sleep(2)
#for-loop --opdracht 1
for i in range(len(fruit)):
    print(fruit[i])
    time.sleep(1.5)
#Dit is het einde van opdracht 1. Over naar opdracht 2



# -- Opdracht 2
#
# -- 2.1. Asking the user for the hour of the local time

print("Please give me a time in hours.")
time.sleep (2)
print("You can choose between 0-23")
time.sleep (2)

#While True loop
#Ik heb toegevoegd dat alles tussen 0-5 nacht is en alles vanaf 6 ochtend is.
#Ook heb ik de optie om exit te typen toegevoegd.

while True:
    try:
        invoer = input("Wat is het huidige uur? (0-23 of typ 'exit' om te stoppen): ")

        if invoer.lower() == 'exit':
            print("Programma wordt gestopt.")
            break  # Stop de while-loop

        uur = int(invoer)

        if 0 <= uur <= 5:
            print("Het is nacht")
        elif 6 <= uur <= 11:
            print("Het is ochtend")
        elif 12 <= uur <= 17:
            print("Het is middag")
        elif 18 <= uur <= 23:
            print("Het is avond")
        else:
            print("Je hebt een ongeldig uur ingevuld!")
    except ValueError:
        print("Ongeldige invoer! Vul een getal in of typ 'exit' om te stoppen.")
