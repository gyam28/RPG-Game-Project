class Magic():
    def __init__(self,name, mp_cost, dmg=20,type):
        self.name = name
        self.mp_cost = mp_cost
        self.dmg = dmg
        self.max_dmg = dmg + 15
        self.low_dmg = dmg - 15
        self.type = ["Dark","Light"]

    def generate_magic_dmg(self):
        magic_damage_result = random.randrange(self.low_dmg, self.max_dmg)
        return magic_damage_result
