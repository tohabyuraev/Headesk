import os
import json


tiles_path = os.path.abspath(
    'data/osm/dbase.json')

tiles = dict()

mow_path = os.path.abspath(
    'data/osm/mow'
)
kzn_path = os.path.abspath(
    'data/osm/kzn'
)
z_list = os.listdir(
    mow_path
)
for z in z_list:
    # Времменый словарь для сбора
    # имен изображений по папкам x
    # для каждой папки z
    tiles_ = dict()
    _z_path = os.path.join(
        mow_path, str(z)
    )
    x_list = os.listdir(
        _z_path
    )
    for x in x_list:
        _x_path = os.path.join(
            _z_path, str(x)
        )
        y_list = os.listdir(
            _x_path
        )
        tiles_[x] = y_list
    tiles[z] = tiles_
    del tiles_

with open(tiles_path, 'w') as fout:
    json.dump(tiles, fout)

if '619' in tiles['10']:
    print('Содержится')
