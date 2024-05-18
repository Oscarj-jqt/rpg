import new
import time

def create_character():

    global player_data, PV, attack, defense
    player_data = {"x": 0, "y": 0}  # Réinitialiser les coordonnées au milieu de la forêt

    print(f"{name}, choisissez le type de personnage que vous souhaitez être :")
    print("1. Tank")
    print("2. Éclaireur")
    print("3. Sniper")

    character_choice = int(input("Choisissez un type (1-3) : "))

    while character_choice < 1 or character_choice > 3:
        print("Erreur ! Veuillez entrer un nombre entre 1 et 3.")
        character_choice = int(input("Choisissez un type : "))

    time.sleep(0.5)

    if character_choice == 1:
        print(f"Félicitations, {name} ! Vous devenez un Tank, solide comme un roc !")
        PV = 3500
        attack = 300
        defense = 400
    elif character_choice == 2:
        print(f"{name}, vous devenez un Éclaireur, rusé et sage comme un renard ! ")
        PV = 2200
        attack = 500
        defense = 150
    elif character_choice == 3:
        print(f"{name}, vous devenez un Sniper, agile et précis comme un Zinedine Zidane !")
        PV = 1500
        attack = 900
        defense = 50
    elif character_choice == "exit":
      exit_game()

    character_data = {
        "name": name,
        "class": character_choice,
        "PV": PV,
        "Attack": attack,
        "Defense": defense,
    }

    time.sleep(0.5)

    print(f"C'est parti, {name} ! Vous êtes maintenant prêt à vous frotter à ceux qui vous ont mené ici.")
    return character_data
    print(character_data)
