### This code contains the tkinter's widget of the programme

from tkinter import *

### Creation of the reference window

window = Tk()
window.title("Le Monty Hall")
window.geometry('1500x900') 

### widgets for the initialization

picture_face = PhotoImage(file='pictures_monty_hall/face.png')

label_picture_init = Label(window)
label_initialize = Label(window)

button_lancer = Button(window)

### widget for the main game

picture_closed_door = PhotoImage(file='pictures_monty_hall/close.png')
picture_open_goat = PhotoImage(file='pictures_monty_hall/open_goat.png')
picture_open_treasure = PhotoImage(file='pictures_monty_hall/open_treasure.png')
picture_showing = PhotoImage(file='pictures_monty_hall/showing.png')

label_door_1 = Label(window)
label_door_2 = Label(window)
label_door_3 = Label(window)

