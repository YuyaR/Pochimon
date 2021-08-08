from .gui import attack_gui
import time
import random
import sys


def slow_print(message: str, typing_speed=200):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0/typing_speed)
    print('')


class Pokemon:
    def __init__(self, name: str, hp: int,
                 attack: int, defense: int,
                 elemental_type: str, moves: list = None):
        self.hp = hp
        self.name = name
        self.attack = attack
        self.defense = defense
        self.fainted = False
        self.elemental_type = ElementalType(elemental_type)
        if moves is None:
            self.moves = []
            self.moves.append(Attack('Pound', 40, 30, 'Normal'))
        else:
            if len(moves) > 4:
                raise ValueError('Pokemon can\'t learn more than four moves')
            else:
                self.moves = moves
        self.move_names = [x.name for x in self.moves]

    def fight(self, other):
        idx = attack_gui(self.move_names)
        move = self.moves[idx]
        slow_print(f'{self.name} used {move}')
        element = [move.elemental_type, other.elemental_type]
        element_name = [move.elemental_type.element,
                        other.elemental_type.element]

        if element_name[0] == 'Normal' or element_name[1] == 'Normal':
            other.hp -= (self.attack * move.power) / other.defense

        elif element[0] > element[1]:
            other.hp -= 2 * (self.attack * move.power) / other.defense
            slow_print("It's super effective!")

        elif element[0] < element[1] or element[0] == element[1]:
            other.hp -= 0.5 * (self.attack * move.power) / other.defense
            slow_print("It's not very effective...")

        else:
            other.hp -= (self.attack * move.power) / other.defense

        move.pp -= 1
        if other.hp <= 0:
            other.hp = 0
            slow_print(f'{other.name} has fainted')
            other.fainted = True
            return False

        return True

    def __repr__(self):
        return self.name


class Attack:
    def __init__(self, name: str, power: int,
                 max_pp: int, elemental_type: str):
        self.name = name
        self.power = power
        self.pp = max_pp
        self.max_pp = max_pp
        self.elemental_type = ElementalType(elemental_type)

    def __repr__(self):
        return self.name


class ElementalType:
    def __init__(self, element: str):
        possible = ['Grass', 'Fire', 'Water', 'Normal']
        if element.capitalize() not in possible:
            raise ValueError(f"{element.capitalize()} not available")
        else:
            self.element = element.capitalize()
        self.winner = [('Grass', 'Water'),
                       ('Fire', 'Grass'),
                       ('Water', 'Fire')]

    def __gt__(self, other):
        return (self.element, other.element) in self.winner

    def __eq__(self, other):
        return self.element == other.element

    def __lt__(self, other):
        return (other > self)
