"""
Program: first_gui.py
Author: Jessie Horvath
Date Modified: 03/20/2022

The purpose of this program is to create a graphical
user interface (GUI) that allows a user to make a choice
and triggers an event within the GUI.
"""
import tkinter
from turtle import width
def on_click():
    label.config(text="Good choice")

m = tkinter.Tk()

m.title("Favorite Meal")
breakfast = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=breakfast, command=on_click).grid(row=1)

second_breakfast = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Second Breakfast", variable=second_breakfast, command=on_click).grid(row=2)

lunch = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Lunch", variable=lunch, command=on_click).grid(row=3)

dinner = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Dinner", variable=dinner, command=on_click).grid(row=4)

label = tkinter.Label(m, text="Waiting")
label.grid(row=5)

button = tkinter.Button(m, text="Exit", width=30, command=m.destroy)
button.grid(row=6)

m.mainloop()