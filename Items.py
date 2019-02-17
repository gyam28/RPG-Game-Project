import random
class Items():
    def __init__ (self,name,description, qty, type, mp=0, hp=0, dmg=0):
        self.name = name
        self.description = description
        self.quantity = qty
        self.type = type
        self.mp_gain = mp
        self.hp_gain = hp
        self.dmg = dmg
