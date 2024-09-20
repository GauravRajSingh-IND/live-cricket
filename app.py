import os
import tkinter

from dotenv import load_dotenv
from fetch_data import Fetch_Data

class UserInterface:

    load_dotenv()

    def __init__(self):

        self.cric_obj = Fetch_Data(os.getenv('rapid_api_key'), os.getenv('radip_api_host'), os.getenv('end_point_cricketbuzz'))
        self.cric_data = self.cric_obj.get_matches(event_type= "live")
        self.internation_series_names_live = self.get_series_name()

        self.window = tkinter.Tk()
        self.window.title("Cricket Buzz")
        self.window.geometry("1200x800")
        self.window.config(bg="lavender")

        # add title.
        self.title = tkinter.Label(self.window, text= "Live Cricket Score - Scorecard and Match Results", font= ('arial', 30, 'bold'),
                                   bg="lavender", foreground= "black")
        self.title.place(x=250, y=50)

        # Live events.
        self.live_canvas = tkinter.Canvas(self.window, bg= "gainsboro", width= 300, height= 600, highlightthickness= 1)
        self.live_canvas.create_text(150, 30, text= "LIVE", font= ('arial', 25, 'bold'), fill= "gray20")
        self.live_canvas.place(x=100, y=150)

        # Recent events.
        self.recent_canvas = tkinter.Canvas(self.window, bg= "gainsboro", width= 300, height= 600, highlightthickness= 1)
        self.recent_canvas.create_text(150, 30, text= "RECENT", font= ('arial', 25, 'bold'), fill= "gray20")
        self.recent_canvas.place(x= 450, y=150)

        # Upcoming event.
        self.upcoming_canvas = tkinter.Canvas(self.window, bg= "gainsboro", width= 300, height= 600, highlightthickness= 1)
        self.upcoming_canvas.create_text(150, 30, text= "UPCOMING", font= ('arial', 25, 'bold'), fill= "gray20")
        self.upcoming_canvas.place(x= 800, y=150)

    def exit(self):
        self.window.mainloop()

    def check_international_matches(self, data):
        length = len(data)
        for i in range(length):
            if self.internation_live['typeMatches'][i]['matchType'] == "International":
                return i

    def get_series_name(self):

        self.internation_live = self.cric_data['response']
        self.internation_live_number = self.check_international_matches(self.internation_live)
        self.internation_live = self.internation_live['typeMatches'][self.internation_live_number]

        data = self.internation_live

        num_series = len(data['seriesMatches'])
        series = {}

        for i in range(num_series):
            try:
                name = data['seriesMatches'][i]['seriesAdWrapper']['seriesName']
                id = data['seriesMatches'][i]['seriesAdWrapper']['seriesId']

                if id not in series:
                    series[id] = name
            except:
                pass

        return series

app = UserInterface()
app.exit()