#!/usr/bin/env python3

import sys
import os
import time

# Functie om scherm te wissen
def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

# Functie om tekst langzaam te typen
def typer(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Start
typer("initializing................100% OK")

# --- WHILE LOOP OPDRACHT ---
typer("Hello, how are you?")
typer("I will ask you a positive number. Please only give positive ones")
time.sleep(2.5)
clr()

#typer("The Loop -")  # debugging
totaal = 0
getal = int(input("Please give me a positive number: "))

while getal > 0:
    totaal += getal
    getal = int(input("Please give me a positive number: "))

time.sleep(2)
print("The total is:" ,totaal)

# --- FOR LOOP OPDRACHT ---
#print("The For -")  # debugging
time.sleep(1.5)

# - Aantal keer invoeren en controleren op positieve waarden.
while True:
    try:
        aantal = int(input("Hoeveel getallen wil je invoeren?: "))
        if aantal <= 0: 
            print("Voer een positief aantal in.")
            continue
        break
    except ValueError:
        print("Ongeldige invoer. Voer een geheel getal in.")

totaal = 0

# - Getallen invoeren (keer 't aantal) en invoer controleren of numerieke INT waarden.
for i in range(aantal):
    while True:
        try:
            getal = int(input(f"Voer getal {i + 1}e in: ")) # Counter i + 1 
            totaal += getal
            break
        except ValueError:
            print("Ongeldige invoer. Voer een geheel getal in.")

print("De som van de getallen is:", totaal)


# --- FOR LOOP Versie 2 ---
# -- 
clr()
typer("The For - Versie 2 -")  # debugging
print("Uitgbreide meldingen.")  # debugging
time.sleep(1.5)

# - Aantal keer invoeren en controleren op positieve waarden.

while True:
    try:
        aantal = int(input("Hoeveel getallen wil je invoeren?: "))
        if aantal <= 0:
            print("Ongeldige invoer: het aantal moet een positief geheel getal zijn groter dan nul.")
            continue
        break
    except ValueError:
        print("Ongeldige invoer: je moet een geheel getal invoeren, bijvoorbeeld 3 of 10.")

totaal = 0
getallen = [] # Getallen opslaan in een ARRAY

# - Getallen invoeren (keer 't aantal) en invoer controleren of numerieke INT waarden.
for i in range(aantal):
    while True:
        try:
            getal = int(input(f"Voer geheel getal {i + 1} in (mag negatief zijn): "))
            getallen.append(getal)
            totaal += getal
            break
        except ValueError:
            print(f"Ongeldige invoer bij getal {i + 1}: voer een geldig geheel getal in, zoals -5, 0 of 12.")

# Resultaten tonen

print("\n Resultaten:")
print("Ingevoerde getallen:", getallen)
print("Som van de getallen:", totaal)
print("Gemiddelde waarde:", totaal / aantal)
print("Hoogste getal:", max(getallen))
print("Laagste getal:", min(getallen))