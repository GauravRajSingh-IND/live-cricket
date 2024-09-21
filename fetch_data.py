import os
import requests
from dotenv import load_dotenv

# load environment data.
load_dotenv()

class Fetch_Data:

    VALID_EVENT_TYPE = {"live", "recent", "upcoming"}

    def __init__(self, key:str, host:str, end_point:str):

        self.api_key = key
        self.api_host = host
        self.api_end_point = end_point
        self.event_type = "live"

    def get_matches(self, event_type:str = "live"):
        """
        This function returns list of event for live, recent and upcoming cricket matches.
        by default event type is live event.
        :param event_type: type of events, live, recent, upcoming.
        :return:
        """

        # assign event type.
        if event_type not in self.VALID_EVENT_TYPE:
            return {"is_fetched": False, "response": f"Invalid event type: {event_type}, Valid options are: {self.VALID_EVENT_TYPE}"}
        self.event_type = event_type

        url =f"{self.api_end_point}{self.event_type}"

        headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": self.api_host
        }

        try:
            matches = requests.get(url= url, headers=headers)
            matches.raise_for_status()

            # validate response.
            data = matches.json()
            return {"is_fetched": True, "response":data}

        except requests.RequestException as e:
            return {"is_fetched":False, "response":{e}}

    def get_ranking(self, format_type:str, format_category:str):
        """
        This function return ranking of the given format type and category.
        :param format_type: odi, test, t20
        :param format_category: batsmen, baller, all-rounder
        :return: dict response
        """

        url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/{format_category}?formatType={format_type}"

        headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": self.api_host
        }

        try:
            ranking = requests.get(url= url, headers=headers)
            ranking.raise_for_status()

            # validate response.
            data = ranking.json()
            return {"is_fetched": True, "response":data}

        except requests.RequestException as e:
            return {"is_fetched":False, "response":{e}}

    def get_series_data(self, url:str, key: str, host: str, series_id: int) -> dict:
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
            "x-rapidapi-host": host
        }

        try:
            series_data = requests.get(url=end_point, headers=headers)
            series_data.raise_for_status()

            return {"is_fetched": True, "response": series_data.json()}

        except requests.RequestException as e:
            return {"is_fetched": False, "response": {e}}

    def get_series_matches(self, series_data):
        """
        This function takes series data and return number of matches played in the series
        :param series_data:
        :return:
        """

        length = len(series_data['matchDetails'])

        number_matches = 0
        date = []
        match_id = []
        match_desc = []
        match_format = []
        match_state = []
        match_status = []
        # loop over each list to check number of matches.
        for match in range(length):

            # check keys
            if 'matchDetailsMap' in series_data['matchDetails'][match].keys():
                number_matches += 1
                date.append(series_data['matchDetails'][match]['matchDetailsMap']['key'])
                match_id.append(
                    series_data['matchDetails'][match]['matchDetailsMap']['match'][0]['matchInfo']['matchId'])
                match_desc.append(
                    series_data['matchDetails'][match]['matchDetailsMap']['match'][0]['matchInfo']['matchDesc'])
                match_format.append(
                    series_data['matchDetails'][match]['matchDetailsMap']['match'][0]['matchInfo']['matchFormat'])
                match_state.append(
                    series_data['matchDetails'][match]['matchDetailsMap']['match'][0]['matchInfo']['state'])
                match_status.append(
                    series_data['matchDetails'][match]['matchDetailsMap']['match'][0]['matchInfo']['status'])

        return {"Number_Matches": number_matches, "date": date, "match_id": match_id, "match_description": match_desc,
                "match_format": match_format, "match_state": match_state, "match_status": match_status}

# app = Fetch_Data(os.getenv('rapid_api_key'), os.getenv('radip_api_host'), os.getenv('end_point_cricketbuzz'))
# test = app.get_matches("recent")
# print(test)
