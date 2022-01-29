from io import BytesIO

import requests
from PIL import Image

from get_from_address import get_point_from_address
from get_from_search import get_from_search
from get_from_static import get_from_static
from lonlat_distance import lonlat_distance
from snippet import snippet


def main() -> None:
    point_address = get_point_from_address()
    address_ll = ",".join(map(str, point_address))
    response = get_from_search(address_ll)

    if not response:
        raise requests.ConnectionError

    response, point_pharmacy = get_from_static(response, address_ll)
    if not response:
        raise requests.ConnectionError

    distance = lonlat_distance(point_address, point_pharmacy)
    snippet.append(f'Расстояние до аптеки — {distance}')
    Image.open(BytesIO(response.content)).show()

    print(*snippet, sep='\n')


if __name__ == '__main__':
    main()
