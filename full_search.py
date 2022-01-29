from io import BytesIO
import requests
from PIL import Image

from create_param_for_static_api import create_static_api_params


def main():
    # python search.py Москва, ул. Ак. Королева, 12
    map_params = create_static_api_params()
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    Image.open(BytesIO(response.content)).show()


if __name__ == '__main__':
    main()
