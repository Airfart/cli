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
typer(".........................OK")

# --- WHILE LOOP OPDRACHT ---
typer("Hello, how are you?")
typer("I will ask you a positive number. Please only give positive ones")
time.sleep(2.5)
clr()

typer("The Loop -")  # debugging
totaal = 0
getal = int(input("Please give me a positive number: "))

while getal > 0:
    totaal += getal
    getal = int(input("Please give me a positive number: "))

time.sleep(2)
print("De som van de positieve getallen is:", totaal)

# --- FOR LOOP OPDRACHT ---
print("The For -")  # debugging
time.sleep(1.5)

aantal = int(input("Hoeveel getallen wil je invoeren?: "))
totaal = 0

for i in range(aantal):
    getal = int(input(f"Voer getal {i + 1} in: "))
    totaal += getal

print("De som van de getallen is:", totaal)
