# Subclasses, parent classes. Make tigers from cats :)

import lesson_21 as cats

class PredatorCatC(cats.CatC):
    "This cats are aggressive and they have predators attributes."
    big_toothes = True
    big_claws = True
    predator = True
    predator_states = ['hunting']

    def get_info(self):
        super().get_info()
        print(f"This cat is predator and has big toothes and big claws.")

tiger = PredatorCatC()