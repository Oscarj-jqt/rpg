import time
import random
import new
import create

name = ''
player_data = {"x": 0, "y": 0}  # Coordonnées initiales du personnage
boss_location = {"x": 0, "y": 5}  # Coordonnées de la caverne du boss
forest_zone_location = {"x": 0, "y": 1}  # Coordonnées de la zone forestière
item_zone_location = {"x": 0, "y": -5}



def move():
    global player_data

    print(f"{name}, vous vous déplacez dans la forêt...")

    # Vérifier si le joueur est à la caverne du boss
    if player_data == boss_location:
        print("Vous êtes à la caverne du boss. Soyez prêt pour le combat final !")
        boss_encounter()  # Appel de la fonction pour le combat contre le boss
        return  # Sortir de la fonction move après le combat contre le boss



    # Demander au joueur où il souhaite se déplacer ensuite
    next_location = input("Où souhaitez-vous aller ? \n q. gauche \n d. droite \n z. avant \n s. arrière ")

    # Ajouter la logique pour gérer le déplacement vers le nouvel endroit
    if next_location == "q":
        player_data["x"] -= 0
    elif next_location == "d":
        player_data["x"] += 0
    elif next_location == "z":
        player_data["y"] += 1
    elif next_location == "s":
        player_data["y"] -= 1
    elif next_location == "exit":
        exit_game()
    else:
        print("Direction invalide. Vous restez à votre emplacement actuel.")

    # Gestion des événements en fonction des coordonnées actuelles
    x, y = player_data["x"], player_data["y"]
    if x == 0 and y > 0:
        forest_event()
    elif x == 0 and y > -5:
        item_event()
    elif x == boss_location["x"] and y == boss_location["y"]:
        boss_encounter()  # Appel de la fonction pour le combat contre le boss
        return  # Sortir de la fonction move après le combat contre le boss

    move()  # Appel récursif pour le prochain déplacement

