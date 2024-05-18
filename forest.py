import random

def forest_event():
    print("Vous explorez la zone forestière. Soyez très attentif, les sbires du boss rodent ici, cette zone est infesté, il va falloir se montrer très discret")

    # Déterminer aléatoirement l'événement en fonction des probabilités
    event_probability = random.randint(1, 100)

    if event_probability <= 50:
        fight()
    elif 50 < event_probability <= 90:
        print("Vous ne trouvez rien d'intéressant.")
    else:
        find_inventory()