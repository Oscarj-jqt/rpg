import time
import random

# Déclaration des variables globales
XP = 0
level = 1
XP_required_for_next_level = 100



def gain_XP(amount):
    global XP, level, XP_required_for_next_level, attack, defense, PV

    XP += amount
    print(f"Vous avez gagné {amount} XP !")

    if XP >= XP_required_for_next_level:
        level_up()

def level_up():
    global XP, level, XP_required_for_next_level, attack, defense, PV

    print(f"Félicitations ! Vous avez atteint le niveau {level} !")

    # Augmentation des statistiques du joueur
    attack += 50
    defense += 50
    PV += 500

    # Réinitialisation de l'XP et mise à jour du niveau requis pour le prochain niveau
    XP -= XP_required_for_next_level
    level += 1
    XP_required_for_next_level = int(XP_required_for_next_level * 1.5)

    print(f"Vos statistiques ont augmenté ! Attaque : {attack}, Défense : {defense}, PV : {PV}")
    print(f"Prochain niveau à {XP_required_for_next_level} XP.")
