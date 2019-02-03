import Person

def calculate_damage(attacker,receiver):
    damage_given = attacker.generate_dmg()
    receiver.take_dmg(damage_given)
    print(f"{attacker.name} gave {damage_given} Pts of damage to {receiver.name}! ")

#Player attack
def playerTurn():
    while True:
        print("\nSelect one of the following actions:")
        player.choose_action()
        action_number = int(input(">>>"))
        if 1 <= action_number and action_number <= len(player.actions):
            break

    action = player.actions[action_number-1]
    if action == "Attack":
        print("Attacking the enemy!")
        calculate_damage(player,enemy)

#Enemy attack
def enemyTurn():
    print("Enemy's Turn!")
    calculate_damage(enemy,player)

def printGameStatus():
    print("--------------------------------------")
    player.get_stat()
    enemy.get_stat()
    print("--------------------------------------")

def checkForWinner():
    if player.hp <= 0:
        print(f"\tGame over! {enemy.name} won the battle!")
        return True
    elif enemy.hp <= 0:
        print("\tVictory! The Evil has been defeated!")
        return True


player = Person.Person("Good Ash",100,200,20)
enemy = Person.Person("EvilDead",100,200,20)

# INTRODUCTION TO GAME:

print("--------------------------------------")
print("\tWelcome to Ash Vs the Evil Dead!")
print("\tLet's fight the Evil Dead!")
printGameStatus()

game_over = False

while not game_over:
    playerTurn()
    enemyTurn()
    printGameStatus()
    game_over = checkForWinner()
