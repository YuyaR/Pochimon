from Game import Pokemon
from Game import Trainer
from Game import pokeapi

# use pokestat to instantiate
pokedex = []

pokelist = pokeapi.get_pokemon(11)
pokelist.update(pokeapi.get_pokemon('pikachu'))


for po in list(pokelist.keys()):
    hp = pokelist[po]['hp']
    attack = pokelist[po]['attack']
    defense = pokelist[po]['defense']
    pokedex.append(Pokemon.Pokemon(po.capitalize(), hp, attack, defense, 'Normal'))

print(pokedex[1])
# for obj in pokedex:
#     print(obj.name)

# satoshi = trainer.Trainer(pokedex[6:])
# shigeru = trainer.Trainer(pokedex[1:6])
# print(satoshi.pokemon)
# print(shigeru.pokemon)

# Pound = pokemon.Attack('Pound', 40, 30, 30, 'normal')
# FireBlast = pokemon.Attack('Fire Blast', 100, 10, 10, 'Fire')
# Thunder = pokemon.Attack('Thunder', 120, 5, 5, 'fire')
# Jump = pokemon.Attack('Jump', 0, 40, 40, 'normal')

# pikachu = pokemon.Pokemon('Pikachu', 200, 30, 20, 'Normal', [Pound, FireBlast, Thunder])
# bulbasaur = pokemon.Pokemon('Bulbasaur', 200, 30, 20, 'Grass')
# magikarp = pokemon.Pokemon('Magikarp', 150, 10, 10, 'Water', Jump)

# while True:
#     if pikachu.hp>0:
#         pikachu.fight(bulbasaur)
#     else:
#         print("Pikachu is incapacitated!")
#     if bulbasaur.hp>0:
#         bulbasaur.fight(pikachu)
#     else:
#         print("Bulbasaur is incapacitated!")
#         break

