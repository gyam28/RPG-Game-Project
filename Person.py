class Person():
    def __init__ (self,name,hp=200,mp=200,attack=20):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.attack = attack
        self.actions = ["Attack","Magic"]
        self.atk_high = attack + 10
        self.atk_low = attack - 10

class Magic():
    def __init__ (self, name, mp_cost, dmg=20, type):
        self.name = name
        self.mp_cost = mp_cost
        self.dmg = dmg
        self.max_dmg = dmg + 15
        self.low_dmg = dmg - 15
        self.type = ["Dark","Light"]


    def get_stat(self):
        print(f"{self.name}:\t{self.hp}/{self.max_hp} HP \n\t\t{self.mp}/{self.max_mp} MP")

    def generate_dmg(self):
        damage_result = random.randrange(self.atk_low,self.atk_high)
        return damage_result

    def take_dmg(self, taken_damage):
        hp_left = self.hp - taken_damage
        return hp_left

    def choose_action(self):
        #actions can be (1)Physical attack or (2)Magic

        action = 1
        for element in self.actions:
            print(f"{action}. {element}")
            action = action + 1

    def generate_magic_dmg(self):
        magic_damage_result = random.randrange(self.low_dmg, self.max_dmg)
        return magic_damage_result
