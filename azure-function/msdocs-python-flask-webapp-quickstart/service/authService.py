import os
import requests
import logging


def authorize():
    try:
        response = requests.post(
            'https://api.chartmetric.com/api/token',
            data = {'refreshtoken':os.getenv("CHARTMETRIC_SECRET")},
        )
        return response.json()['token']
    except requests.exceptions.RequestException as e:
        logging.error(e)
    except requests.exceptions.HTTPError as f:
        logging.error(f)
        print(f.response.text)
    

        