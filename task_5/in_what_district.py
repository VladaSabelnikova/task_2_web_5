
from task_5.get_from_address import get_point_from_address
from task_5.get_from_geocoder import get_from_geocoder


def main() -> None:
    address_ll = get_point_from_address()
    response = get_from_geocoder(','.join(map(str, address_ll)))
    if response:
        json_response = response.json()
        district = json_response['response'][
            'GeoObjectCollection']['featureMember'][0]['GeoObject']['name']
        print(district)


if __name__ == '__main__':
    main()
