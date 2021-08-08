from typing import Union
from typing import Dict
import requests

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
