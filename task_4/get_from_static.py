from typing import List, Union, Tuple

import requests
from requests import Response


def get_from_static(
    response: requests,
    *args: Tuple
) -> List[Union[Response, List[float]]]:

    output = []

    json_response = response.json()
    organizations = json_response["features"][:10]
    for organization in organizations:
        org_opening_hours = organization["properties"]["CompanyMetaData"][
            'Hours']['text']

        point = organization["geometry"]["coordinates"]
        org_point = f"{point[0]},{point[1]}"

        color = 'wt' if not org_opening_hours else 'bl'

        if org_opening_hours == 'ежедневно, круглосуточно':
            color = 'gn'

        output.append([point, f'{org_point},pm2{color}l'])

    return output
