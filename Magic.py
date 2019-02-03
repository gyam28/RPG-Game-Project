import random
class Magic():
    def __init__ (self,name, mp_cost, dmg=20,type):
        self.name = name
        self.mp_cost = mp_cost
        self.dmg = dmg
        self.max_dmg = dmg + 15
        self.low_dmg = dmg - 15
        self.type = type

    def generate_magic_dmg(self):
        return random.randrange(self.low_dmg, self.max_dmg)
