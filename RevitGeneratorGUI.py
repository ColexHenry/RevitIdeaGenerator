#####################################################################################################################################
#GUI Version of Program 
#####################################################################################################################################

#!/usr/bin/python
import random as r
from tkinter import *
from tkinter import ttk 

#Defines Main Window name(title) and size(geometry)
root = Tk()
root.title("Revit Building Idea Generator") 
root.geometry("500x400") 

x = Label(root, text="Welcome to the Revit Building Idea Generator").place(x = 120, y = 20) # Welcome message

y = Label(root, text="Click the button to generate Revit Building Ideas!").place(x = 90, y = 70) # Brief Description

def main():
    a = r.randint(1, 5) # Bedrooms Values
    b = r.randint(1, 2) # Bathrooms Values
    c = r.randint(1, 1) # Living Rooms Values
    d = r.randint(1, 1) # Kitchens Values
    SpecialFeatureList = ['Bay Window','Fireplace','Kitchen Island','Walk-in Closet','Personal Theater','Mud Room','Garage','Backyard/Porch','Balcony','Vaulted Ceiling'] #Special Feature List
    e = r.choice(SpecialFeatureList) # Randomly chooses SpecialFeatureList item (Ex: Bay Window, Fireplace, etc)

    Label(root, text=f"Bedrooms: {a} ").place(x = 90, y = 115) # Display Bedrooms in window
    Label(root, text=f"Bathrooms: {b} ").place(x = 90, y = 145) # Display Bathrooms in window
    Label(root, text=f"Living Rooms: {c} ").place(x = 90, y = 175) # Display Living Rooms in window
    Label(root, text=f"Kitchens: {d} ").place(x = 90, y = 205) # Display Living Rooms in window
    Label(root, text=f"Special Features: {e}              ").place(x = 90, y = 235) # Display Living Rooms in window


main()
z = Button(root, text="Generate Building Idea", command=main, highlightcolor='green').place(x = 80, y = 320) # Button to generate new building idea
z = Button(root, text="Quit", command=root.destroy, highlightcolor='red').place(x = 350, y = 320) #button for quitting program





#Makes Tkinter run main program Window
root.mainloop()



