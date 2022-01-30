import requests
from requests import Response


def get_from_static_api(
    type_l: str,
    low_corn: str,
    up_corn: str,
    address_ll: str = '',
    spn: str = '0.005,0.005',
) -> Response:

    map_params = {
        "l": type_l,
        "bbox": f'{low_corn}~{up_corn}',
        "ll": address_ll,
        "spn": spn

    }

    if not address_ll:
        del map_params['ll']
        del map_params['spn']
    else:
        del map_params['bbox']

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    return response
