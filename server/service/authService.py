import os
import requests


def authorize():
    response = requests.post(
            'https://api.chartmetric.com/api/token',
            data = {'refreshtoken':os.getenv("CHARTMETRIC_SECRET")},
        )
    return response.json()['token']