from widgets import *

def effacer_init():
    label_picture_init.place_forget()
    label_initialize.place_forget()
    button_lancer.place_forget()
    
def partie():
    
    label_door_1.image = picture_closed_door
    label_door_1.configure(image = picture_closed_door)
    label_door_2.image = picture_closed_door
    label_door_2.configure(image = picture_closed_door)
    label_door_3.image = picture_closed_door
    label_door_3.configure(image = picture_closed_door)
    
    label_door_1.place(x='300', y='300')
    label_door_2.place(x='700', y = '300')
    label_door_3.place(x='1100', y='300')

def initialize():
    
    label_initialize['text'] = """ 
    Bienvenue dans le jeu du MONTY-HALL!\n
    Vous ferez face à trois portes. L'une de ces portes cache un trésor! les deux autres cachent une chèvre.\n
    Bien sur, votre objectif consistera à trouver le trésor.\n
    Le jeu se déroule en deux étapes. Vous commencerez par désigner une porte, le présentateur ouvrira alors une autre porte, qui cachait une chèvre.\n
    Vous devrez alors prendre une décision: rester sur votre choix de porte initial, ou désigner la porte restante.\n
    À vous de choisir quelle stratégie vous semble la plus judicieuse!
    """
    label_picture_init.image = picture_face 
    label_picture_init.configure(image = picture_face) 
    button_lancer['text'] = "Cliquez pour lancer le jeu"
    button_lancer['command'] = lambda: [effacer_init(), partie()]
    
    label_picture_init.place(x='750', y='50')
    label_initialize.place(x='300', y = '400')
    button_lancer.place(x='750', y='600')
    


