import random


def numbering():

    name = give_name()
    print(f"Hello {name} ")


def give_name():
    names = ["Toni", "Monika", "Ivan"]
    return random.choice(names)

numbering()
numbering()
numbering()
