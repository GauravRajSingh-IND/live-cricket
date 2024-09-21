# import requests
# import os
#
# from dotenv import load_dotenv
#
# def get_series_data(url:str, key:str, host:str, series_id:int) -> dict:
#     """
#     This function takes series id and fetch the data the series.
#     :param url: end point.
#     :param key: api key
#     :param host: api host
#     :param series_id: series id, should be integer
#     :return: return dictionary object.
#     """
#
#     series_id = series_id
#     end_point = f"{url}{series_id}"
#
#     headers = {
#         "x-rapidapi-key": key,
#         "x-rapidapi-host":host
#     }
#
#     try:
#         series_data = requests.get(url=end_point, headers=headers)
#         series_data.raise_for_status()
#
#         return {"is_fetched": True, "response":series_data.json()}
#
#     except requests.RequestException as e:
#         return {"is_fetched": False, "response": {e}}
#
#
# load_dotenv()
#
# id =  os.getenv('rapid_api_key')
# host = os.getenv('radip_api_host')
# url = os.getenv('end_point_series')
#
# series_data = get_series_data(url=url, key=id, host=host, series_id=3641)
# print(series_data)


series_data = {'is_fetched': True, 'response':
    {'matchDetails': [{'matchDetailsMap': {'key': 'Fri, 20 May 2022 - Mon, 23 May 2022',
                                           'match': [{'matchInfo': {'matchId': 48002, 'seriesId': 3641, 'seriesName': 'New Zealand tour of England, 2022',
                                                                    'matchDesc': '1st Warm-up Match', 'matchFormat': 'TEST', 'startDate': '1653040800000', 'endDate': '1653300000000', 'state': 'complete', 'status': 'Match drawn',
                                                                    'team1': {'teamId': 41, 'teamName': 'SUSSEX', 'teamSName': 'SUS', 'imageId': 172148},
                                                                    'team2': {'teamId': 13, 'teamName': 'NEW ZEALAND', 'teamSName': 'NZ', 'imageId': 172128},
                                                                    'venueInfo': {'ground': 'County Ground', 'city': 'Hove', 'timezone': '+01:00'}, 'currBatTeamId': 13, 'isTimeAnnounced': True},
                                                      'matchScore': {'team1Score': {'inngs1': {'inningsId': 2, 'runs': 247, 'wickets': 10, 'overs': 79.1}},
                                                                     'team2Score': {'inngs1': {'inningsId': 1, 'runs': 342, 'wickets': 3, 'overs': 90.0, 'isDeclared': True}, 'inngs2': {'inningsId': 3, 'runs': 40, 'overs': 8.0}}}}], 'seriesId': 3641}}, {'adDetail': {'name': 'native_news_index_random_1', 'layout': 'native_large', 'position': 1}}, {'matchDetailsMap': {'key': 'Thu, 26 May 2022 - Sun, 29 May 2022', 'match': [{'matchInfo': {'matchId': 48009, 'seriesId': 3641, 'seriesName': 'New Zealand tour of England, 2022', 'matchDesc': '2nd Warm-up Match', 'matchFormat': 'TEST', 'startDate': '1653559200000', 'endDate': '1653818400000', 'state': 'complete', 'status': 'County Select XI won by 7 wkts', 'team1': {'teamId': 886, 'teamName': 'COUNTY SELECT XI', 'teamSName': 'CSXI', 'imageId': 174284}, 'team2': {'teamId': 13, 'teamName': 'NEW ZEALAND', 'teamSName': 'NZ', 'imageId': 172128}, 'venueInfo': {'ground': 'County Ground', 'city': 'Chelmsford', 'timezone': '+01:00'}, 'currBatTeamId': 886, 'isTimeAnnounced': True}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 2, 'runs': 247, 'wickets': 10, 'overs': 74.2}, 'inngs2': {'inningsId': 4, 'runs': 264, 'wickets': 3, 'overs': 88.0}}, 'team2Score': {'inngs1': {'inningsId': 1, 'runs': 362, 'wickets': 9, 'overs': 100.0, 'isDeclared': True}, 'inngs2': {'inningsId': 3, 'runs': 148, 'wickets': 10, 'overs': 43.2}}}}], 'seriesId': 3641}}, {'matchDetailsMap': {'key': 'Thu, 02 Jun 2022 - Mon, 06 Jun 2022', 'match': [{'matchInfo': {'matchId': 38326, 'seriesId': 3641, 'seriesName': 'New Zealand tour of England, 2022', 'matchDesc': '1st Test', 'matchFormat': 'TEST', 'startDate': '1654164000000', 'endDate': '1654509600000', 'state': 'complete', 'status': 'England won by 5 wkts', 'team1': {'teamId': 9, 'teamName': 'ENGLAND', 'teamSName': 'ENG', 'imageId': 172123}, 'team2': {'teamId': 13, 'teamName': 'NEW ZEALAND', 'teamSName': 'NZ', 'imageId': 172128}, 'venueInfo': {'ground': "Lord's", 'city': 'London', 'timezone': '+01:00'}, 'currBatTeamId': 9, 'isTimeAnnounced': True}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 2, 'runs': 141, 'wickets': 10, 'overs': 42.5}, 'inngs2': {'inningsId': 4, 'runs': 279, 'wickets': 5, 'overs': 78.5}}, 'team2Score': {'inngs1': {'inningsId': 1, 'runs': 132, 'wickets': 10, 'overs': 40.0}, 'inngs2': {'inningsId': 3, 'runs': 285, 'wickets': 10, 'overs': 91.3}}}}], 'seriesId': 3641}}, {'matchDetailsMap': {'key': 'Fri, 10 Jun 2022 - Tue, 14 Jun 2022', 'match': [{'matchInfo': {'matchId': 38331, 'seriesId': 3641, 'seriesName': 'New Zealand tour of England, 2022', 'matchDesc': '2nd Test', 'matchFormat': 'TEST', 'startDate': '1654855200000', 'endDate': '1655200800000', 'state': 'complete', 'status': 'England won by 5 wkts', 'team1': {'teamId': 9, 'teamName': 'ENGLAND', 'teamSName': 'ENG', 'imageId': 172123}, 'team2': {'teamId': 13, 'teamName': 'NEW ZEALAND', 'teamSName': 'NZ', 'imageId': 172128}, 'venueInfo': {'ground': 'Trent Bridge', 'city': 'Nottingham', 'timezone': '+01:00'}, 'currBatTeamId': 9, 'isTimeAnnounced': True}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 2, 'runs': 539, 'wickets': 10, 'overs': 128.2}, 'inngs2': {'inningsId': 4, 'runs': 299, 'wickets': 5, 'overs': 50.0}}, 'team2Score': {'inngs1': {'inningsId': 1, 'runs': 553, 'wickets': 10, 'overs': 145.3}, 'inngs2': {'inningsId': 3, 'runs': 284, 'wickets': 10, 'overs': 84.4}}}}], 'seriesId': 3641}}, {'adDetail': {'name': 'native_news_index_random_2', 'layout': 'native_large', 'position': 4}}, {'matchDetailsMap': {'key': 'Thu, 23 Jun 2022 - Mon, 27 Jun 2022', 'match': [{'matchInfo': {'matchId': 38332, 'seriesId': 3641, 'seriesName': 'New Zealand tour of England, 2022', 'matchDesc': '3rd Test', 'matchFormat': 'TEST', 'startDate': '1655978400000', 'endDate': '1656324000000', 'state': 'complete', 'status': 'England won by 7 wkts', 'team1': {'teamId': 9, 'teamName': 'ENGLAND', 'teamSName': 'ENG', 'imageId': 172123}, 'team2': {'teamId': 13, 'teamName': 'NEW ZEALAND', 'teamSName': 'NZ', 'imageId': 172128}, 'venueInfo': {'ground': 'Headingley', 'city': 'Leeds', 'timezone': '+01:00'}, 'currBatTeamId': 9, 'isTimeAnnounced': True}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 2, 'runs': 360, 'wickets': 10, 'overs': 67.0}, 'inngs2': {'inningsId': 4, 'runs': 296, 'wickets': 3, 'overs': 54.2}}, 'team2Score': {'inngs1': {'inningsId': 1, 'runs': 329, 'wickets': 10, 'overs': 117.3}, 'inngs2': {'inningsId': 3, 'runs': 326, 'wickets': 10, 'overs': 105.2}}}}], 'seriesId': 3641}}], 'appIndex': {'seoTitle': 'New Zealand tour of England, 2022 live scores, schedule and results - Cricbuzz | Cricbuzz.com', 'webURL': 'www.cricbuzz.com/cricket-series/'}}}


