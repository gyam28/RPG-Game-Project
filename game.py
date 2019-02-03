import Person

player = Person.Person("Good Ash",200,200,20)
enemy = Person.Person("EvilDead",200,200,20)

# INTRODUCTION TO GAME:

print("--------------------------------------")
print("\tWelcome to Ash Vs the Evil Dead!")
print("\tLet's fight the Evil Dead!")
player.get_stat()
enemy.get_stat()
print("--------------------------------------")

while True:
    print("\nSelect one of the following actions:")
    player.choose_action()
    action_number = input(">>>")
    if 1 <= action_number && action_number <= player.actions.count():
        break

action = player.actions[action_number-1]
if action == "Attack":
    print("Attacking the enemy!")
    damage_given = player.generate_dmg()
    enemy.take_dmg(damage_given)
    print(f"{player.name} gave {damage_given} Pts of damage to {enemy.name}! ")
    player.get_stat()
    enemy.get_stat()

#Enemy turn
