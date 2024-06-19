#!/usr/bin/python3
import random as r
from tkinter import *


########################
#CLI Version of Program 
########################


#Prints welcome message and takes user input
print("Welcome to the Revit Building Generator")

print()
print("Type Start or Quit")
print()
t = str(input("Enter Here: ")) 
print()




#Creates main function that shows rooms for building
def main():
    while True:
        if t.lower() == "start": #.lower for ignoring case 
            a = r.randint(1, 5) # Bedrooms
            b = r.randint(1, 2) # Bathrooms
            c = r.randint(1, 1) # Living Rooms
            d = r.randint(1, 1) # Kitchens
            SpecialFeatureList = ['Bay Window', 'Fireplace', 'Kitchen Island', 'Walk-in Closet', 'Personal Theater', 'Mud Room', 'Garage', 'Backyard/Porch', 'Balcony'] #Special Feature List
            e = r.choice(SpecialFeatureList) #Randomly chooses SpecialFeatureList list item
            print("Results")
            print()
            print(f"Bedrooms: {a} ")
            print(f"Bathrooms: {b} ")
            print(f"Living Rooms: {c} ")
            print(f"Kitchens: {d} ")
            print(f"The Special Feature is a {e} ")
            print()
            print()
            g = str(input("Would you like to try again? (Y or N): "))
            print()
            if g.lower() == "y": #.lower for ignoring case
                main()
            else:
                if g.lower() == "n": #.lower for ignoring case
                    print("Goodbye")
                    print()
            break

        else: 
            if t.lower() == "quit":
                print("Goodbye")
                print()
                break




#Calls main function to be displayed
main()
