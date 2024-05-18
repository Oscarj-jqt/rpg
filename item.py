import random

def item_event():
    print("Vous explorez la zone d'objets...")

    # Déterminer aléatoirement l'événement en fonction des probabilités
    event_probability = random.randint(1, 100)

    if event_probability <= 60:
        find_inventory()
        move()
    elif 60 < event_probability <= 90:
        print("Vous ne trouvez rien d'intéressant.")
        move()
    else:
        fight()
