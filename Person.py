import random

class Person():
    def __init__ (self,name,magics,hp=200,mp=200,attack=20):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.attack = attack
        self.actions = ["Attack","Magic","Heal"]
        self.atk_high = attack + 10
        self.atk_low = attack - 10
        self.magics = magics

    def get_stat(self):
        print(f"{self.name}:\t{self.hp}/{self.max_hp} HP \n\t\t{self.mp}/{self.max_mp} MP")

    def generate_dmg(self):
        damage_result = random.randrange(self.atk_low,self.atk_high)
        return damage_result #can be also randint(self.atk_low,self.atk_high

    def take_dmg(self, taken_damage):
        self.hp = self.hp - taken_damage
        if self.hp < 0:
            self.hp = 0

    def choose_action(self):
        #actions can be (1)Physical attack, (2)Magic or (3)Self Healing
        action = 1
        for element in self.actions:
            print(f"\n{action}. {element}")
            action = action + 1

    def reduce_mp(self,used_mp):
        self.mp = self.mp - used_mp
        return self.mp

    def available_magic(self):
        options_left = []
        for magic in self.magics:
            if self.mp >= magic.mp_cost:
                options_left.append(magic)
        return options_left

    def choose_magic(self):
        action = 1
        magic_left = self.available_magic()
        for element in magic_left:
            print(f"\n{action}. {element.name}")
            action = action + 1
