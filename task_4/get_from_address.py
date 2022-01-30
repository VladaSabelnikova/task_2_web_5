import sys
from typing import List

import requests

ADDRESS = toponym_to_find = " ".join(sys.argv[1:])


def get_point_from_address(toponym_to_find: str = ADDRESS) -> List[float]:
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"
    }

    response = requests.get(geocoder_api_server, params=geocoder_params)
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        toponym_coodrinates = toponym["Point"]["pos"]

        toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

        return [float(toponym_longitude), float(toponym_lattitude)]
    raise requests.ConnectionError
