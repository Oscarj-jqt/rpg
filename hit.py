def hit():
    global PV, monster_PV, attack, monster_defense

    monster_PV -= max(0, attack - monster_defense)
    time.sleep(0.5)
    print("Bien joué, il ne lui reste plus que", max(0, monster_PV), "PV \n Tu lui as causé", attack-monster_defense,"dégâts")
    return monster_PV

def monster_hit():
    global PV, monster_attack, defense

    print("Attention, il riposte !! \n Il t'a causé", max(0,monster_attack-defense),"dégats")
    time.sleep(0.5)
    PV -= max(0, monster_attack - defense)
    return PV
