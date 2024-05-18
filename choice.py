import random

inventory_type = ["Potion", "Boost Attack", "Boost Defense"]
my_inventory = ["couteau"]

def find_inventory():
    if len(my_inventory) < 5:
        new_inventory = random.choice(inventory_type)
        my_inventory.append(new_inventory)
        print("Ouahhh super ! Tu as trouvé un(e)", new_inventory, "!")
        print("Inventaire actuel :", my_inventory)

    else:
        print("Désolé, tu ne peux pas porter plus de 5 objets. Tu devrais peut-être utiliser certains avant d'en trouver de nouveaux.")
        print("Te voila équipé, dirige toi vers le nord il va falloir que tu affronte tes ennemis pour sortir d'ici")

    move()
