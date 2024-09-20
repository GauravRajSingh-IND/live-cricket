import os
import requests
from dotenv import load_dotenv

# load environment data.
load_dotenv()

class Fetch_Data:

    VALID_EVENT_TYPE = {"live", "recent", "upcoming"}

    def __init__(self):

        self.api_key = os.getenv('rapid_api_key')
        self.api_host = os.getenv('radip_api_host')
        self.api_end_point = os.getenv('end_point_cricketbuzz')

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

# app = Fetch_Data()
# test = app.get_matches("recent")
# print(test)
