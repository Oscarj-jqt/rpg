boost_attack_duration = 0
boost_defense_duration = 0
couteau_duration = 0


def inventory():
    global PV, attack, defense
    global boost_attack_duration, boost_defense_duration, couteau_duration

    print("Inventaire actuel :", my_inventory)

    if not my_inventory:
        print("Votre inventaire est vide.")
        return

    item_choice = int(input("Choisissez un objet (1-" + str(len(my_inventory)) + ") : "))

    while item_choice < 1 or item_choice > len(my_inventory):
        print("Veuillez entrer un nombre entre 1 et", len(my_inventory))
        item_choice = int(input("Choisissez un objet : "))

    selected_item = my_inventory[item_choice - 1]

    print("Vous utilisez", selected_item)

    if selected_item == "Boost Attack":
        print("Votre attaque est boostée pendant 2 tours !")
        boost_attack_duration = 2
        while boost_attack_duration > 0 :
          attack *= 2
          return
        reduce_inventory_durations()
    elif selected_item == "Boost Defense":
        print("Votre défense est boostée pendant 2 tours !")
        boost_defense_duration = 2
        defense *= 2
        reduce_inventory_durations()
    elif selected_item == "Potion":
        global PV
        print("Vous avez récupéré 800 points de vie !")
        PV += 800
        print("Il te reste", PV, "PV.")
    elif selected_item == "couteau":
        global monster_defense
        print("Coup critique !!")
        couteau_duration = 2
        monster_defense = 0
        boss_defense = 0
        attack *= 2
        reduce_inventory_durations()

    # Retire l'élément utilisé de l'inventaire
    my_inventory.remove(selected_item)




def reduce_inventory_durations():
    global boost_attack_duration, boost_defense_duration, couteau_duration, attack, defense, monster_defense, boss_defense

    if boost_attack_duration > 0:
        boost_attack_duration -= 1
        if boost_attack_duration == 0:
            print("L'effet de Boost Attack a expiré.")
            attack = attack / 2

    if boost_defense_duration > 0:
        boost_defense_duration -= 1
        if boost_defense_duration == 0:
            print("L'effet de Boost Defense a expiré.")
            defense = defense / 2

    if couteau_duration > 0:
        couteau_duration -= 1
        if couteau_duration == 0:
            print("L'effet du couteau a expiré.")
            attack //= 2
            monster_defense = 100
            boss_defense = 800


