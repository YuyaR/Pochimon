import os
from typing import Union
from typing import Dict
import requests
import urllib.request

ROOT = 'https://pokeapi.co/api/v2/pokemon/'

def get_pokemon(x: Union[str, int]) -> Dict:
    if isinstance(x, str):
        pokename = x.lower()
    elif isinstance(x, int):
        pokename = str(x)
    else:
        raise ValueError('Please, enter a pokemon name or a valid integer')

    link = ROOT + pokename
    r = requests.get(link)
    pname = r.json()['name']
    pokestat = {pname: {}}
    
    for n in range(0, 3):
        stat = r.json()['stats'][n]['base_stat']
        stat_type = r.json()['stats'][n]['stat']['name']
        pokestat[pname][stat_type] = stat

    pokestat[pname]['elemental_type'] = \
        r.json()['types'][0]['type']['name']

    return pokestat


def download_pokemon_sprite(x: str) -> None:
    '''
    x: str
        Name of the pokemon
    '''
    pokename = x.lower()

    os.makedirs(f'sprites/{pokename}', exist_ok=True)

    front = f'https://pokemon-sprites.s3.amazonaws.com/{pokename}/front.png'
    back = f'https://pokemon-sprites.s3.amazonaws.com/{pokename}/back.png'
    urllib.request.urlretrieve(front, f'sprites/{pokename}/front.png')
    urllib.request.urlretrieve(back, f'sprites/{pokename}/back.png')


if __name__ == '__main__':
    download_pokemon_sprite('ivysaur')
