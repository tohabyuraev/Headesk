import os
import json
import sys
from random import (
    choice,
)
from urllib3 import (
    PoolManager,
)
from typing import (
    NamedTuple,
)
from concurrent.futures import (
    ThreadPoolExecutor,
)

from mercantile import (
    tiles,
)


class Area(NamedTuple):
    n: float
    e: float
    s: float
    w: float
    z: float


mow_area = Area(
    n = 36.853,
    e = 55.415,
    s = 38.359,
    w = 56.067,
    z = 17,
)

mow_tiles = list(
    tiles(*mow_area)
)

data_path = os.path.join(
    os.path.abspath('./'), 'data'
)
tiles_path = os.path.abspath(
    'data/osm/dbase.json'
)
with open(tiles_path, 'rb') as fin:
    dbase = json.load(fin)

osm_path = os.path.join(
    data_path, 'osm'
)
googlen_path = os.path.join(
    data_path, 'googlen'
)
googles_path = os.path.join(
    data_path, 'googles'
)

#  Создание папок в Googlen!
mow_path = os.path.join(
    osm_path, 'mow'
)
if not os.path.isdir(data_path):
    os.makedirs(data_path)
if not os.path.isdir(osm_path):
    os.makedirs(osm_path)
if not os.path.isdir(googlen_path):
    os.makedirs(googlen_path)
if not os.path.isdir(googles_path):
    os.makedirs(googles_path)
if not os.path.isdir(mow_path):
    os.makedirs(mow_path)

z_list = set(
    [tile.z for tile in mow_tiles]
)
for z in z_list:
    _z_dir_path = os.path.join(
        mow_path, str(z)
    )
    if not os.path.isdir(_z_dir_path):
        os.makedirs(_z_dir_path)
    x_list = set(
        [tile.x for tile in mow_tiles if tile.z == z]
    )
    for x in x_list:
        _x_dir_path = os.path.join(
            _z_dir_path, str(x)
        )
        if not os.path.isdir(_x_dir_path):
            os.makedirs(_x_dir_path)

m = PoolManager()
def dwload(tile):
    if f'{tile.y}.png' not in dbase.get(
        f'{tile.z}'
    ).get(
        f'{tile.x}'
    ):
        r = m.request(
            'GET',
            f"http://{choice(['a', 'b', 'c'])}.tile.openstreetmap.org"
            f'/{tile.z}'
            f'/{tile.x}'
            f'/{tile.y}.png'
        )
        img_path = os.path.join(
            'osm',
            mow_path,
            str(tile.z),
            str(tile.x),
            str(tile.y) + '.png'
        )
        with open(img_path, 'wb') as fout:
            fout.write(r.data)
    else: pass


with ThreadPoolExecutor(max_workers=16) as executor:
    executor.map(dwload, mow_tiles)