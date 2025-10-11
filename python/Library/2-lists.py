#!/usr/bin/env python3

# Opdracht CS leerjaar 1 - Opdracht ?
#
# Status: Ingeleverd
#
# Omschrijving: Lists

import time

#Variabelen lijsten
temperaturen=["0", "10", "20"]
sport=["voetbal", "zeilen", "schaken"]

#Colors
RED = "\033[31m"
GREEN = "\033[32m"
WHITE = "\033[37m"
RESET = "\033[0m"

#Print eerste temperatuur uit de lijst
print ("First I will print the first tempature")
time.sleep (2)
print(temperaturen[0])
time.sleep (1.5)

#Print tweede temperatuur uit de lijst
print("I will now print the second tempature of the list")
time.sleep (2)
print(temperaturen[1])
time.sleep (1.5)

#Voeg een nieuwe temperatuur toe aan de lijst
print(f"{GREEN}I will now add a tempature to the list")
time.sleep (2)
temperaturen.append("30")
time.sleep (2)
print(f"{RED}Added 30 to the list")
time.sleep (1)

#Verwijder een temperatuur uit de lijst
print("Now lets remove 10 out of the list")
time.sleep (1.5)
temperaturen.remove("10")
time.sleep (2)
print(f"{GREEN}Tempatures are now: " + " , ".join(temperaturen))
time.sleep (1)

#Laat het aantal items in de lijst zien
print("The number of items in the list is:", len(temperaturen))
time.sleep (2)
print(f"{RED}Now going to the second part The SPORTLISTS")
print("PLEASE WAIT 5 SECONDS")
time.sleep (5)
#Sportlists
print("Welcome to Sportlists")

#First item from list
print(f"{GREEN}First i will print the first item of the list")
time.sleep (2)
print(sport[0])
time.sleep (2.5)

#Second item from the list
print(f"{RED}Now I will print the second item of the list")
time.sleep (2)
print(sport[1])
time.sleep (2.5)

#Add a item to the list
print(f"{GREEN}now I will add a sport to the sport list")
time.sleep (0.5)
print("Lets add Tennis!!!")
time.sleep (2)
sport.append("Tennis")
time.sleep (1.5)

#Remove a sport of the list
print(f"{RED}Now lets remove a sport of the list")
time.sleep (1.5)
print("Lets remove Tennis!!!")
time.sleep (2)
sport.remove("Tennis")
time.sleep (1.5)

#How many sports are in the list?
print(f"{RESET}Now at last but not least,")
time.sleep (2)
print("How many sports have remained the python script?")
time.sleep (2)
print("THE ANSWER ISSS: ",len(sport))
time.sleep (2.5)
print("The sports that have REMAINED ARE: " + " , ".join(sport))
time.sleep (2)
print(f"{RED}Goodbye")