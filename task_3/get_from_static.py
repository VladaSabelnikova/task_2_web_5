from typing import Tuple, List

import requests
from requests import Response

from snippet import snippet


def get_from_static(
    response: requests,
    address_ll: str
) -> Tuple[Response, List[float]]:

    json_response = response.json()
    organization = json_response["features"][0]

    org_name = organization["properties"]["CompanyMetaData"]["name"]
    org_address = organization["properties"]["CompanyMetaData"]["address"]
    org_opening_hours = organization["properties"]["CompanyMetaData"][
        'Hours']['text']

    point = organization["geometry"]["coordinates"]
    org_point = f"{point[0]},{point[1]}"

    map_params = {
        "l": "map",
        "pt": f"{org_point},pm2dgl~{address_ll},pm2dgl"
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response_static = requests.get(map_api_server, params=map_params)

    snippet.append(f'Название аптеки — {org_name}')
    snippet.append(f'Адрес аптеки — {org_address}')
    snippet.append(f'Часы работы аптеки — {org_opening_hours}')

    return response_static, point
