from typing import List

import requests


def get_corn_from_address(toponym_to_find: str) -> List[str]:
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"
    }

    response = requests.get(geocoder_api_server, params=geocoder_params)
    if response:
        json_response = response.json()
        corners = json_response['response']['GeoObjectCollection'][
            'featureMember'][0]['GeoObject']['boundedBy']['Envelope']

        low_corn = ','.join(corners['lowerCorner'].split())
        up_corn = ','.join(corners['upperCorner'].split())

        return [low_corn, up_corn]
    raise requests.ConnectionError


def get_address_ll_from_address(toponym_to_find: str) -> str:
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

        return ','.join([toponym_longitude, toponym_lattitude])
    raise requests.ConnectionError
