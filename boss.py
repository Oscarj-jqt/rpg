# Initialisation des statistiques du boss
boss_PV = 5000
boss_attack = 700
boss_defense = 700

def boss_encounter():
    global PV, name

    print(f"Vous êtes face au terrifiant boss ! Préparez-vous au combat final, {name}!")



    while PV > 0 and boss_PV > 0:
        print(f"\nStatut du combat : {name} : {max(0, PV)} PV | Boss : {max(0, boss_PV)} PV")

        # Ajoutez ici d'autres détails spécifiques au combat contre le boss, si nécessaire.

        time.sleep(1)
        choice = input("Que veux-tu faire ?\n1. Attaquer\n2. Utiliser l'inventaire\n3. Fuir\n")

        while not choice.isdigit() or not 1 <= int(choice) <= 3:
            print("Veuillez entrer un nombre entre 1 et 3.")
            choice = input("Choisissez une option : ")

        choice = int(choice)

        if choice == 1:
            hit_boss()
            time.sleep(0.5)
            if boss_PV > 0:
                time.sleep(0.5)
                boss_hit()
        elif choice == 2:
            time.sleep(0.5)
            inventory()
            boss_hit()
        elif choice == "exit":
            exit_game()
        else:
            time.sleep(0.5)
            print("Impossible de fuir du combat contre le boss !")
            boss_hit()

        print(f"Il reste {max(0, PV)} PV à {name} et {max(0, boss_PV)} PV au boss.")

    if PV <= 0:
        time.sleep(0.5)
        print("Perdu, le boss t'a vaincu...")
        main_menu()
    elif boss_PV <= 0:
        time.sleep(0.5)
        print("Félicitations, tu as vaincu le redoutable boss !!!")

    print("Le combat contre le boss est terminé.")
    main_menu()


def boss_hit():
    global PV, name

    print("Attention, le boss riposte !")
    time.sleep(0.5)
    PV -= max(0, boss_attack - defense)

    return PV

def hit_boss():
    global PV, boss_PV, attack, boss_defense

    boss_PV -= max(0, attack - boss_defense)
    time.sleep(0.5)
    print("Il ne lui reste plus que", max(0, boss_PV), "PV \n Tu lui a causé", max(0, attack-boss_defense),"dégâts")
    return boss_PV
