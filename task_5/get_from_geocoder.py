import requests


def get_from_geocoder(address_ll: str) -> requests:
    api_server = "https://geocode-maps.yandex.ru/1.x/"
    api_key = "40d1649f-0493-4b70-98ba-98533de7710b"

    search_params = {
        "apikey": api_key,
        "lang": "ru_RU",
        "geocode": address_ll,
        "kind": "district",
        "format": "json"
    }

    response = requests.get(api_server, params=search_params)

    return response
