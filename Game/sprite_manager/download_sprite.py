import os
import urllib.request


def download_pokemon_sprite(x: str) -> None:
    '''
    x: str
        Name of the pokemon
    '''
    pokename = x.lower()

    os.makedirs(f'data/sprites/{pokename}', exist_ok=True)

    front = f'https://pokemon-sprites.s3.amazonaws.com/{pokename}/front.png'
    back = f'https://pokemon-sprites.s3.amazonaws.com/{pokename}/back.png'
    urllib.request.urlretrieve(front, f'sprites/{pokename}/front.png')
    urllib.request.urlretrieve(back, f'sprites/{pokename}/back.png')

