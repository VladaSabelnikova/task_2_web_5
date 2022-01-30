import pathlib
import random

import requests

from get_point_from_address import get_corn_from_address, \
    get_address_ll_from_address
from get_from_static_api import get_from_static_api


def show_img(city_name):
    low_corn, up_corn = get_corn_from_address(city_name)
    type_l = random.choice(['sat', 'map'])
    address_ll = ''

    if type_l == 'map':
        address_ll = get_address_ll_from_address(city_name)
    response = get_from_static_api(type_l, low_corn, up_corn, address_ll)

    if not response:
        raise requests.ConnectionError

    map_file = pathlib.Path('map.png')
    map_file.write_bytes(response.content)

    return map_file
