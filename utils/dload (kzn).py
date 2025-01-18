import os
from urllib3 import (
    PoolManager,
)
from typing import (
    NamedTuple,
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


kzn_area = Area(
    n = 48.815,
    e = 55.684,
    s = 49.377,
    w = 55.931,
    z = 9,
)

kzn_tiles = list(
    tiles(*kzn_area)
)

data_path = os.path.join(
    os.path.abspath('./'), 'data'
)
kzn_path = os.path.join(
    data_path, 'kzn'
)
if not os.path.isdir(data_path):
    os.makedirs(data_path)
if not os.path.isdir(kzn_path):
    os.makedirs(kzn_path)

z_list = set(
    [tile.z for tile in kzn_tiles]
)
for z in z_list:
    _z_dir_path = os.path.join(
        kzn_path, str(z)
    )
    if not os.path.isdir(_z_dir_path):
        os.makedirs(_z_dir_path)
    x_list = set(
        [tile.x for tile in kzn_tiles if tile.z == z]
    )
    for x in x_list:
        _x_dir_path = os.path.join(
            _z_dir_path, str(x)
        )
        if not os.path.isdir(_x_dir_path):
            os.makedirs(_x_dir_path)

m = PoolManager()
for tile in kzn_tiles:
    r = m.request(
        'GET',
        f'http://b.tile.openstreetmap.org'
        f'/{tile.z}'
        f'/{tile.x}'
        f'/{tile.y}.png'
    )
    img_path = os.path.join(
        'osm',
        kzn_path,
        str(tile.z),
        str(tile.x),
        str(tile.y) + '.png'
    )
    with open(img_path, 'wb') as fout:
        fout.write(r.data)
