import sys

import requests


def create_static_api_params():
    toponym_to_find = " ".join(sys.argv[1:])
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"
    }

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        raise requests.ConnectionError

    json_response = response.json()

    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]

    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]

    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    corners = json_response['response']['GeoObjectCollection'][
        'featureMember'][0]['GeoObject']['boundedBy']['Envelope']

    low_corn = ','.join(corners['lowerCorner'].split())
    up_corn = ','.join(corners['upperCorner'].split())

    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "bbox": f'{low_corn}~{up_corn}',
        "l": "map",
        "pt": f'{",".join([toponym_longitude, toponym_lattitude])},,pm2dgl'
    }

    return map_params
