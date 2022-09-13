### This code contains the tkinter's widget of the programme

from tkinter import *
import random

### variable for doors features

doors_features = {}

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

label_info = Label(window)

dict_info_score = {"nb_try":0, "nb_goat": 0, "nb_treasure":0}

label_nb_try = Label(window)
label_nb_goat = Label(window)
label_nb_treasure = Label(window)


picture_closed_door = PhotoImage(file='pictures_monty_hall/close.png')
picture_open_goat = PhotoImage(file='pictures_monty_hall/open_goat.png')
picture_open_treasure = PhotoImage(file='pictures_monty_hall/open_treasure.png')
picture_showing = PhotoImage(file='pictures_monty_hall/showing.png')

label_door_1 = Label(window)
label_door_2 = Label(window)
label_door_3 = Label(window)

button_door_1 = Button(window)
button_door_2 = Button(window)
button_door_3 = Button(window)

### widget for the choice

label_showing = Label(window)
button_change = Button(window)
button_keep = Button(window)
button_goend = Button(window)

picture_point = PhotoImage(file='pictures_monty_hall/point.png')

label_point = Label(window)

### widget for the end game

picture_genius = PhotoImage(file='pictures_monty_hall/genius.png')
picture_crying = PhotoImage(file='pictures_monty_hall/crying.png')
picture_treasure = PhotoImage(file='pictures_monty_hall/treasure.png')
picture_goat = PhotoImage(file='pictures_monty_hall/goat.png')

label_picture_end = Label(window)
label_picture_reward = Label(window)

label_text_end = Label(window)

button_redo = Button(window)

button_simulate_100_keep = Button(window)
button_simulate_100_change = Button(window)

### widget for the simulation

picture_old = PhotoImage(file='pictures_monty_hall/old.png')
label_picture_simulation = Label(window)
label_simulation = Label(window)







