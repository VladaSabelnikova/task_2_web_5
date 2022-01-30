from io import BytesIO

import requests
from PIL import Image

from get_from_address import get_point_from_address
from get_from_search import get_from_search
from get_from_static import get_from_static


def main() -> None:
    point_address = get_point_from_address()
    address_ll = ",".join(map(str, point_address))
    response = get_from_search(address_ll)

    if not response:
        raise requests.ConnectionError

    all_pt = []

    for point_pharmacy, pt in get_from_static(response):
        all_pt.append(pt)

    map_params = {
        "l": "map",
        "pt": '~'.join(all_pt + [f'{address_ll},home'])
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    Image.open(BytesIO(response.content)).show()


if __name__ == '__main__':
    main()
