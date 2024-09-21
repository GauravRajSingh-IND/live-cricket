import requests
import os

from dotenv import load_dotenv

def get_series_data(url:str, key:str, host:str, series_id:int) -> dict:
    """
    This function takes series id and fetch the data the series.
    :param url: end point.
    :param key: api key
    :param host: api host
    :param series_id: series id, should be integer
    :return: return dictionary object.
    """

    series_id = series_id
    end_point = f"{url}{series_id}"

    headers = {
        "x-rapidapi-key": key,
        "x-rapidapi-host":host
    }

    try:
        series_data = requests.get(url=end_point, headers=headers)
        series_data.raise_for_status()

        return {"is_fetched": True, "response":series_data.json()}

    except requests.RequestException as e:
        return {"is_fetched": False, "response": {e}}


load_dotenv()

id =  os.getenv('rapid_api_key')
host = os.getenv('radip_api_host')
url = os.getenv('end_point_series')

series_data = get_series_data(url=url, key=id, host=host, series_id=3641)
print(series_data)