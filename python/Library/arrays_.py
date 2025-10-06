#!/usr/bin/env python3

#Imports
import sys
import os
import time
import __main__
import _thread

#variables of the students
student0= ("Ryan") 
student1= ("Manassih")
student2= ("Mashal")
student3= ("Issam")
studenten = ["Ryan", "Manassih", "Mashal"]

#Colors
RED = "\033[31m"
GREEN = "\033[32m"
WHITE = "\033[37m"
RESET = "\033[0m"

#functions
def clr():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
#The exercise
print (f"{GREEN}the list is " + ", " .join(studenten))
print (f"{GREEN}First I will print the first and last of the list")
time.sleep (2)
print(studenten[0] + "," ,studenten[1])
time.sleep (2)
print (f"{RED}now lets add a student")
time.sleep (1.5)
studenten.append("Issam")
print ("added student Issam: " + ", ".join(studenten))
time.sleep (1)
print (f"{GREEN}Lets remove a student")
time.sleep (2)
studenten.remove ("Issam")
time.sleep (4)
print(f"{RED}Issam is removed")
time.sleep (2)
print("Now lets show the numbers of student that are remained in the list")
time.sleep (2)
print (len(studenten))
time.sleep (4)
clr()
time.sleep (3)
print ("The End")

