from widgets import *

def effacer_init():
    label_picture_init.place_forget()
    label_initialize.place_forget()
    button_lancer.place_forget()

def determine_doors():
    doors_features["treasure_door"] = random.randint(1,3)

def end_game():

    label_door_1.place_forget()
    label_door_2.place_forget()
    label_door_3.place_forget()
    label_showing.place_forget()
    label_info.place_forget()
    button_goend.place_forget()

    text_victory = """
    Félicitation! Vous repartez avec un véritable trésor!
    """

    text_fail = """
    Dommage! Vous repartez avec une chèvre
    """

    if doors_features['victory'] == 1:
        label_picture_end.image = picture_genius
        label_picture_end.configure(image = picture_genius)

        label_picture_reward.image = picture_treasure
        label_picture_reward.configure(image = picture_treasure)

        label_text_end['text'] = text_victory

    elif doors_features['victory'] == 0:
        label_picture_end.image = picture_crying
        label_picture_end.configure(image = picture_crying)

        label_picture_reward.image = picture_goat
        label_picture_reward.configure(image = picture_goat)

        label_text_end['text'] = text_fail

    label_text_end.place(x='100', y='300')
    label_picture_reward.place(x='300', y='400')
    label_picture_end.place(x='500', y='200')

def setup_final_choice(final_choice):
    if doors_features["treasure_door"] == final_choice:
        label_info['text'] = "Magnifique! La porte cachait un trésor!"
        button_goend['text'] = "Super!"
        globals()['label_door_%s' % final_choice].image = picture_open_treasure
        globals()['label_door_%s' % final_choice].configure(image = picture_open_treasure)

        doors_features["victory"] = 1

    elif doors_features["treasure_door"] != final_choice:
        label_info['text'] = "Enfer! La porte cachait une chèvre!"
        button_goend['text'] = "Oh non..."
        globals()['label_door_%s' % final_choice].image = picture_open_goat
        globals()['label_door_%s' % final_choice].configure(image = picture_open_goat)

        doors_features["victory"] = 0

    if final_choice == 1:
        label_showing.place(x='20', y='300')
    elif final_choice == 2:
        label_showing.place(x='450', y='300')
    elif final_choice == 3:
        label_showing.place(x='850', y='300')


def last_choice(choice):
    button_keep.place_forget()
    button_change.place_forget()
    liste_123 = [1,2,3]

    k = doors_features['first_choice']

    if choice == 0:
        final_choice = k
    elif choice == 1:
        label_info['text'] = "Enfer! La porte cachait une chèvre!"
        liste_123.remove(k)
        liste_123.remove(doors_features['showing'])
        final_choice = liste_123[0]

    setup_final_choice(final_choice)

    button_goend['command'] = lambda: end_game()
    button_goend.place(x='700', y='700')

def first_choice(k):

    label_picture_init.place_forget()
    button_door_1.place_forget()
    button_door_2.place_forget()
    button_door_3.place_forget()

    label_showing.image = picture_showing
    label_showing.configure(image = picture_showing)

    doors_features['first_choice'] = k
    treasure_door = doors_features["treasure_door"]
    list_123 = [1,2,3]
    if k == treasure_door:
        list_123.remove(k)
        showing = random.choice(list_123)
    elif k != treasure_door:
        list_123.remove(k)
        list_123.remove(treasure_door)
        showing = list_123[0]
    doors_features['showing'] = showing

    if k == 1:
        mot_k = "première"
    elif k == 2:
        mot_k = "deuxième"
    elif k ==3:
        mot_k = 'troisième'

    if showing == 1:
        mot_showing = "première"
    elif showing == 2:
        mot_showing = "deuxième"
    elif showing ==3:
        mot_showing = 'troisième'

    label_info['text'] = """
    Vous avez choisi la {} porte. Le présentateur ouvre donc la {} porte, révèlant une chèvre hurlante.\n
    Veuillez à présent choisir si vous voulez garder votre choix initial, ou changer de porte.
    """.format(mot_k, mot_showing)
    
    if showing == 1:
        label_door_1.image = picture_open_goat
        label_door_1.configure(image = picture_open_goat)

        label_showing.place(x='20', y='300')

    elif showing == 2:
        label_door_2.image = picture_open_goat
        label_door_2.configure(image = picture_open_goat)

        label_showing.place(x='450', y='300')

    elif showing == 3:
        label_door_3.image = picture_open_goat
        label_door_3.configure(image = picture_open_goat)

        label_showing.place(x='850', y='300')

    button_keep['text'] = "Cliquez ici pour garder votre porte"
    button_keep['command'] = lambda: last_choice(0)

    button_change['text'] = "Cliquez ici pour changer de porte"
    button_change['command'] = lambda: last_choice(1)

    button_change.place(x="500", y="700")
    button_keep.place(x="800", y="700")
    
    
def partie():

    determine_doors()

    label_info['text'] = "Choisissez une porte!"

    label_picture_init.place(x = '20', y = '20')
    label_info.place(x='100', y='20')
    
    label_door_1.image = picture_closed_door
    label_door_1.configure(image = picture_closed_door)
    label_door_2.image = picture_closed_door
    label_door_2.configure(image = picture_closed_door)
    label_door_3.image = picture_closed_door
    label_door_3.configure(image = picture_closed_door)

    button_door_1['text'] = "choisir"
    button_door_1['command'] = lambda: first_choice(1)
    button_door_2['text'] = "choisir"
    button_door_2['command'] = lambda: first_choice(2)
    button_door_3['text'] = "choisir"
    button_door_3['command'] = lambda: first_choice(3)
    
    label_door_1.place(x='300', y='300')
    label_door_2.place(x='700', y = '300')
    label_door_3.place(x='1100', y='300')

    button_door_1.place(x='300', y='600')
    button_door_2.place(x='700', y='600')
    button_door_3.place(x='1100', y='600')

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
    


