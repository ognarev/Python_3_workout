# Game character :)

import random

class Character():
    "Base game character class."
    char_names = ['Mario', 'Luidgy', 'Todd', 'Princess']
    max_live = 100
    
    def __init__(self):
        self.is_live = True
        self.live = self.max_live
        print("Char was born.")
    
    def do_idle(self):
        print("Idling.")

    def do_run(self):
        print("Running.")

    def do_jump(self):
        print("Jumped.")
    
    def do_damage(self, damage=10):
        if self.live - damage <= 0:
            self.do_die()
        else: 
            self.live = self.live - damage
            print("Auch!")
    
    def do_die(self):
        print("I am dead.")
        self.is_dead = True
    
    def do_reborn(self):
        self.__init__()

class MarioChar(Character):
    "Mario game character."    
    name = "Mario"
    max_speed = 4
    max_jump = 4
    max_power = 4

    def __init__(self):
        self.speed = self.max_speed
        self.jump = self.max_jump
        self.power = self.max_power
        print(f"{self.name}")
        super().__init__()    
    
    def do_idle(self):
        print(f"{self.name}")
        return super().do_idle()
    
    def do_run(self):
        print(f"{self.name}")
        return super().do_run()

    def do_jump(self):
        print(f"{self.name}")
        return super().do_jump()

    def do_damage(self, damage=10):
        print(f"{self.name}")
        return super().do_damage(damage)
    
    def do_die(self):
        print(f"{self.name}")
        return super().do_die()
