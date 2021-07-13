#%%
from Game import *
import pokeapi
import os

pokemon_ls = pokeapi.get_pokemon(12)
#%%
# pokemon_dict = {}
# print(pokemon_ls[0].json()['name'])
pok_list = []
for pokemon in pokemon_ls:
    attack = pokeapi.get_attack(pokemon.json())
    defense = pokeapi.get_defense(pokemon.json())
    hp = pokeapi.get_hp(pokemon.json())
    name = pokemon.json()['name']
    new_pok = Pokemon.Pokemon(hp, name=name.upper(), attack=attack, defense=defense, elemental_type='Fire')
    pok_list.append(new_pok)
    # name = pokemon
    # print(f'Attack = {attack}')
    # print(defense)
    # print(hp)
print(pok_list)
#%%
# pound = Pokemon.Attack('Pound', 40, 30, 'Normal')
# ember = Pokemon.Attack('Ember', 40, 20, 'Fire')
# vine_whip = Pokemon.Attack('Vine Whip', 45, 25, 'Grass')
# charmander_moveset = [pound, ember]
# bulbasaur_moveset = [pound, vine_whip]

# charmander = Pokemon.Pokemon(200, 'Charmander', 30, 20, 'Fire', charmander_moveset)
# bulbasaur = Pokemon.Pokemon(200, 'Bulbasaur', 30, 20, 'Grass', bulbasaur_moveset)

# while True:
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print(f'What will {charmander.name} do?')
#     flag = charmander.fight(bulbasaur)
#     if flag == False:
#         break
#     Pokemon.slow_print(f'{bulbasaur.name} has {bulbasaur.hp} points left\n')
#     input('Press Enter to continue')
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print(f'What will {bulbasaur.name} do?')
#     flag = bulbasaur.fight(charmander)
#     if flag == False:
#         break
#     Pokemon.slow_print(f'{charmander.name} has {charmander.hp} points left\n')
#     input('Press Enter to continue')

# %%
