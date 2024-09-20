import os
import tkinter
from tkinter import ttk

from dotenv import load_dotenv
from fetch_data import Fetch_Data

class UserInterface:

    # load environment data.
    load_dotenv()

    def __init__(self):

        self.ranking_format_type = ["test", "odi", "t20"]
        self.ranking_category = ["batsmen", "bowlers", "allrounders", "teams"]

        self.cric_obj = Fetch_Data(os.getenv('rapid_api_key'), os.getenv('radip_api_host'), os.getenv('end_point_cricketbuzz'))

        # self.cric_data = self.cric_obj.get_matches(event_type= "live")
        # self.internation_series_names_live = self.get_series_name()

        self.series = {8393: 'Bangladesh tour of India, 2024', 8818: 'New Zealand tour of Sri Lanka, 2024',
                  8661: 'Afghanistan v South Africa in UAE, 2024', 7572: 'ICC Cricket World Cup League Two 2023-27'}

        self.window = tkinter.Tk()
        self.window.title("Cricket Buzz")
        self.window.geometry("1200x800")
        self.window.config(bg="lavender")

        # add title.
        self.title = tkinter.Label(self.window, text= "Live Cricket Score - Scorecard and Match Results", font= ('arial', 30, 'bold'),
                                   bg="lavender", foreground= "black")
        self.title.place(x=250, y=50)

        # Live events.
        self.live_canvas = tkinter.Canvas(self.window, bg= "gainsboro", width= 750, height= 600, highlightthickness= 1)
        self.live_canvas.create_text(375, 30, text= "LIVE", font= ('arial', 25, 'bold'), fill= "gray20")
        self.display_series(self.series)
        self.live_canvas.place(x=50, y=150)

        self.series_var = tkinter.StringVar()
        self.series_id = tkinter.Entry(self.live_canvas, textvariable= self.series_var, font= ('arial', 20, 'bold'))
        self.series_id.place(x=250, y=500)

        self.live_submit = tkinter.Button(self.live_canvas, text= "Find", font= ('arial', 20, 'bold'), foreground= "black",
                                          command= self.check_series)
        self.live_submit.place(x=550, y=500)

        # Upcoming event.
        self.ranking_canvas = tkinter.Canvas(self.window, bg= "gainsboro", width= 300, height= 600, highlightthickness= 1)
        self.ranking_canvas.create_text(150, 30, text="Ranking", font= ('arial', 25, 'bold'), fill="gray20")

        self.format_type = ttk.Combobox(self.ranking_canvas, values= self.ranking_format_type, font= ('arial', 20, 'bold'))
        self.format_type.current(1)
        self.format_type.place(x=20, y=70)

        self.category_type = ttk.Combobox(self.ranking_canvas, values= self.ranking_category, font= ('arial', 20, 'bold'))
        self.category_type.current(0)
        self.category_type.place(x=20, y=120)

        # get ranking button
        self.ranking_button = tkinter.Button(self.ranking_canvas, text= "Ranking", font= ('arial', 20, 'bold'))
        self.ranking_button.place(x=100, y=170)

        self.ranking_canvas.place(x= 850, y=150)

    def check_series(self):

        id = int(self.series_id.get())

        if id in self.series.keys():
            print(f"Match Found {id}: {self.series[id]}")
        else:
            print("Please check and try again")

    def display_series(self, data):

        # X, y position of text.
        x = 30
        y = 100

        for key, value in data.items():
            self.live_canvas.create_text(x, y, anchor=tkinter.NW, text=f"{key}: {value}",
                                         font= ('arial', 30, 'bold'), fill= "gray20")
            y += 75

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