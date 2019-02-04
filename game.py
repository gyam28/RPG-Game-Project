import Person
import Magic

def calculate_damage(attacker,receiver):
    damage_given = attacker.generate_dmg()
    receiver.take_dmg(damage_given)
    print(f"\n{attacker.name} gave {damage_given} Pts of damage to {receiver.name}! ")

#Player attack
def playerTurn():
    while True:
        print("\nSelect one of the following actions:")
        player.choose_action()
        try:
            action_number = int(input("\n>>>  "))
            if 1 <= action_number and action_number <= len(player.actions):
                break
        except Exception:
            print("\nSomething went wrong!Choose an existing number:")

    action = player.actions[action_number-1]
    if action == "Attack":
        print("\nAttacking the enemy!")
        calculate_damage(player,enemy)
    elif action == "Magic":
        player.choose_magic()
        try:
            magic_number = int(input("\n>>>  "))
            if 1 <= magic_number and magic_number <= len(player.magics):
                magic = player.magics[magic_number-1]
                magic_damage = magic.generate_magic_dmg()
                leftover_mp = player.reduce_mp(magic.mp_cost)
                enemy.take_dmg(magic_damage)
                print(f"\n{player.name} gave {magic_damage} Pts of damage to {enemy.name}! ")
                print(f"\n{player.name} used {magic.name} magic: {leftover_mp} MP is left.")

        except ValueError:
            print("\nSomething went wrong! Choose an existing number:")


#Enemy attack
def enemyTurn():
    print("\nEnemy's Turn!")
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
#magic types
thunder_magic = Magic.Magic("thunder",12,"Light",32)
wind_magic = Magic.Magic("wind",10,"Light",25)
ice_magic = Magic.Magic("ice",8,"Dark",28)
fire_magic = Magic.Magic("fire",10,"Dark",30)
magics = [thunder_magic,ice_magic,wind_magic,fire_magic]

player = Person.Person("Good Ash",magics,100,100,20)
enemy = Person.Person("EvilDead",magics,100,100,20)

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
