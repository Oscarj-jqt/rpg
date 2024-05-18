import create
import time

name = ''

def main_menu():

  print ("1. Nouvelle partie")
  time.sleep(0.5)
  print ("2. Charger partie")
  time.sleep(0.5)
  print ("3. Crédit")
  time.sleep(0.5)
  print ("4. Quitter")
  time.sleep(0.5)
  choice = int(input("Choisissez une option : \n"))

  while choice < 1 or choice > 4:

    print("Erreur ! Veuillez entrer un nombre entre 1 et 4")
    choice = int(input("Choisissez une option : \n"))
    #ajouter si choice n'est pas un nombre

  if choice == 1:
    new_game()
  elif choice == 2:
    load_game()
  elif choice == 3:
    credit()
  elif choice == 4:
    exit_game()




def credit():
    print("Créateurs du jeu \n Aryles \n Hamidou \n Oscar \n Issa")
    main_menu()

def exit_game():
    exit_answer = input("Êtes-vous sûr de vouloir quitter la partie ? (oui/non) ")
    if exit_answer.lower() == "oui":
        print("Merci à bientôt")
        exit()
    elif exit_answer.lower() == "non":
        print("Reprise du jeu")
        main_menu()

def reset_game():
    global PV, my_inventory, boost_attack_duration, boost_defense_duration, couteau_duration, attack, defense, XP, level, XP_required_for_next_level, monster_PV

    # Réinitialiser les points de vie
    PV = 1000  # Remplacez cette valeur par la valeur initiale souhaitée
    attack = 350
    defense = 400
    # Réinitialiser l'inventaire
    my_inventory = ["couteau"]
    XP = 0
    level = 1
    XP_required_for_next_level = 100

    # Réinitialiser les durées des effets des objets
    boost_attack_duration = 0
    boost_defense_duration = 0
    couteau_duration = 0

    print("Nouvelle partie démarrée. Bonne chance, aventurier !")


def new_game():
    reset_game()
    print("Comment t'appelles-tu ?")
    global name
    name = input()
    time.sleep(0.5)
    print("Salut", name, "content de voir que tu es encore en vie. La vie dans cette forêt est rude et il va falloir t'accrocher pour en sortir vivant. J'espère pour toi que tu es prêt !")
    # Assurez-vous d'ajouter les fonctions create_character() et move() ou d'implémenter leur logique ici.
    create_character()
    print("Pour sortir de ce piège à rat, tu n'as qu'une seule solution. Accéder à la sortie qui se situe derrière la caverne du boss. \n Elle se situe au nord de la forêt. Cependant, sache qu'il est très fort et qu'il va falloir t'armer. \n Explore le sud, l'est et l'ouest de la forêt, tu devrais y trouver de quoi de renforcer, mais attention, tu n'es en sécurité nul part ici. \n Tu peux te faire attaquer à tout moment donc bon courage !")
    print("PS : Tu peux quitter la partie en cliquant entrant 'exit' à tout moment")
    move()


