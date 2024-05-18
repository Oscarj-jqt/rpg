
import time
import random

monster_PV = 2500
monster_attack = 500
monster_defense = 150


def fight():
    global PV, name, monster_PV, monster_attack, monster_defense, level, boost_attack_duration, boost_defense_duration, couteau_duration




    tour = 0

    print("Attention, un monstre t'attaque !!! Prépare-toi,", name, "le combat va commencer ! ")

    while PV > 0 and monster_PV > 0:
        tour += 1

        time.sleep(0.5)
        print(f"\nTour {tour} - Statut du combat:")
        time.sleep(0.5)
        print(f"{name}: {max(0, PV)} PV  | Niveau : {level} | Monstre: {max(0, monster_PV)} PV")

        if tour == 3:
            time.sleep(0.5)
            print("N'oublie pas de regarder ton inventaire, il pourrait t'aider à te débarrasser de lui rapidement.")



        choice = input("Que veux-tu faire ?\n1. Attaquer\n2. Utiliser l'inventaire\n3. Fuir\n")

        while not choice.isdigit() or not 1 <= int(choice) <= 3:
            print("Veuillez entrer un nombre entre 1 et 3.")
            choice = input("Choisissez une option : ")

        choice = int(choice)

        if choice == 1:
            hit()
            time.sleep(0.5)
            if monster_PV > 0:
                time.sleep(0.5)
                monster_hit()
        elif choice == 2:
            time.sleep(0.5)
            inventory()
            monster_hit()
        elif choice == "exit":
            exit_game()
        else:
            time.sleep(0.5)
            if random.randint(1, 100) <= 60:  # 60% de chance de réussir à fuir
                escape()
            else:
                print("Le monstre vous rattrape !")
                monster_hit()




        print("Il te reste", max(0, PV), "PV")

    if PV <= 0:
      time.sleep(0.5)
      print("Perdu, tu as été dévoré par les monstres...")
      main_menu()
    elif monster_PV <= 0:
      time.sleep(0.5)
      print("Bien joué, tu lui as mis une belle raclée !!!")
      gain_XP(50)



    # Récupération des points de vie à la fin du combat
    recover_HP = 300
    PV += recover_HP
    monster_PV = monster_max_HP  # Remettre les points de vie du monstre à la valeur maximale

    print("Le combat est terminé.")
    move()

# Ajoutez une variable pour stocker les points de vie max du monstre
monster_max_HP = 3500

def escape():
  print("Tu as réussi à prendre la fuite...")
  move()