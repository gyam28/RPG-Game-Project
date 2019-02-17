import Person
import Magic
import Items
import random
import copy

def calculate_damage(attacker,receiver):
    damage_given = attacker.generate_dmg()
    receiver.take_dmg(damage_given)
    print(f"\n{attacker.name} gave {damage_given} Pts of damage to {receiver.name}! ")

def calculate_magic_damage(magic,attacker,receiver):
    magic_damage = magic.generate_magic_dmg()
    leftover_mp = attacker.reduce_mp(magic.mp_cost)
    if magic.type == "Dark":
        receiver.take_dmg(magic_damage)
        print(f"\n{attacker.name} gave {magic_damage} Pts of damage to {receiver.name}! ")
    else:
        attacker.get_heal(magic_damage)
        print(f"\n{attacker.name} got healed with {magic_damage} HP! ")

    print(f"\n{attacker.name} used {magic.name} magic: {leftover_mp} MP is left.")

def receive_user_input(printingOptions, validationOptions):
    while True:
        print(("*"*50)+("\nSelect one of the following actions:"))
        print(printingOptions)
        try:
            action_number = int(input("\n>>>  "))
            if 1 <= action_number and action_number <= len(validationOptions):
                return action_number
        except Exception:
            print("\nSomething went wrong!Choose an existing number:")

def calculate_item_effect(item,user,receiver):
    if item.type == "potion":
        user.get_heal(item.hp_gain)
        print(f"{user.name} used {item.name} and healed {item.hp_gain}HP!")
    elif item.type == "elixir":
        user.get_heal(item.hp_gain)
        user.get_mana(item.mp_gain)
        print(f"{user.name} used {item.name} to {item.description}!")
    elif item.type == "attack":
        receiver.take_dmg(item.dmg)
        print(f"{user.name} used {item.name} and dealth {item.dmg} damage points to {receiver.name}!")
    leftover_qty = item.quantity -1
    user.updateItems(leftover_qty,item.name)


#Player attack
def playerTurn():
    valid_action = False
    while not valid_action:
        action_number = receive_user_input(player.choose_action(),player.actions)
        action = player.actions[action_number-1]
        if action == "Attack":
            print(("*"*25)+("\nAttacking the enemy!"))
            print("*" * 25)
            calculate_damage(player,enemy)
            valid_action = True
        elif action == "Magic":
            if len(player.available_magic()) == 0:
                print("\nYou have insufficient MP! From now on you only get to attack!")
            else:
                magic_number = receive_user_input(player.choose_magic(),player.available_magic())
                magic = player.available_magic()[magic_number-1]
                calculate_magic_damage(magic,player,enemy)
                valid_action = True
        elif action == "Items":
            if len(player.available_items()) == 0:
                print("\n You have no more available items! Save your life however you can!")
            else:
                item_number = receive_user_input(player.choose_item(),player.available_items())
                item = player.available_items()[item_number -1]
                calculate_item_effect(item, player,enemy)
                valid_action = True


#Enemy attack
def enemyTurn():
    print("\nEnemy's Turn!")
    available_actions = ["Attack"]
    if len(enemy.available_magic()) != 0:
        available_actions.append("Magic")
    if len(enemy.available_items()) != 0:
        available_actions.append("Items")

    actionSelected=random.randint(0,len(available_actions))
    action= available_actions[actionSelected -1]
    print (f"The enemy selected {action}")
    if action == "Attack":
        calculate_damage(enemy,player)
    elif action == "Magic":
        available_magics = enemy.available_magic()
        magicSelected = random.randint(0,len(available_magics))
        magic = available_magics[magicSelected - 1]
        print(f"Enemy used {magic.name}")
        calculate_magic_damage(magic, enemy, player)
    elif action == "Items":
        available_items = enemy.available_items()
        itemSelected = random.randint(0,len(available_items))
        item = available_items[itemSelected - 1]
        print(f"Enemy used {item.name}")
        calculate_item_effect(item, enemy, player)



def printGameStatus():
    print("*" * 50)
    player.get_stat()
    enemy.get_stat()
    print("*" * 50)

def checkForWinner():
    if player.hp <= 0:
        print(f"\tGame over! {enemy.name} won the battle!")
        return True
    elif enemy.hp <= 0:
        print("\tVictory! The Evil has been defeated!")
        return True


#MAGIC types with characteristics: name, mp_cost, type, dmg
thunder_magic = Magic.Magic("thunder",22,"Dark",42)
wind_magic = Magic.Magic("wind",20,"Dark",35)
ice_magic = Magic.Magic("ice",18,"Dark",38)
fire_magic = Magic.Magic("fire",20,"Dark",40)
cure_magic = Magic.Magic("cure",50,"Light",30)
recovery_magic = Magic.Magic("recovery",80,"Light",150)
magics = [thunder_magic,ice_magic,wind_magic,fire_magic,cure_magic,recovery_magic]

#POTIONS characteristics: name,description, quantity, type, mp=0, hp=0, dmg=0
potion = Items.Items("Potion","heals 50HP",qty=15, type="potion",hp=50)
high_potion = Items.Items("High potion","heals 100HP",qty=10, type="potion",hp=100)
super_potion = Items.Items("Super Potion","heals 300HP",qty=5, type="potion",hp=300)
elixir = Items.Items("Elixir","restore max HP and MP", qty=1, type="elixir", hp=1000, mp=1000)
grenade = Items.Items("Grenade","deal 300 damage",qty=2, type="attack", dmg=300)
player_items_lst = [potion, high_potion, super_potion, elixir, grenade]
enemy_items_lst = copy.deepcopy(player_items_lst)

player = Person.Person("Good Ash",magics,player_items_lst, 1000,1000,150)
enemy = Person.Person("EvilDead",magics,enemy_items_lst, 1000,1000,150)

# INTRODUCTION TO GAME:

print("*" * 50)
print("\tWelcome to Ash Vs the Evil Dead!")
print("\tLet's fight the Evil Dead!")
printGameStatus()

game_over = False

while not game_over:
    playerTurn()
    game_over = checkForWinner()
    if not game_over:
        enemyTurn()
        game_over = checkForWinner()
    printGameStatus()
