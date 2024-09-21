import os
import tkinter
from tkinter import ttk

from dotenv import load_dotenv
from fetch_data import Fetch_Data

class UserInterface:

    # load environment data.
    load_dotenv()

    def __init__(self):

        self.series_data = None
        self.ranking_data = None

        self.ranking_format_type = ["test", "odi", "t20"]
        self.ranking_category = ["batsmen", "bowlers", "allrounders", "teams"]

        self.cric_obj = Fetch_Data(os.getenv('rapid_api_key'), os.getenv('radip_api_host'), os.getenv('end_point_cricketbuzz'))

        self.cric_data = self.cric_obj.get_matches(event_type= "live")
        self.internation_series_names_live = self.get_series_name()

        # self.series = {8393: 'Bangladesh tour of India, 2024', 8818: 'New Zealand tour of Sri Lanka, 2024',
        #           8661: 'Afghanistan v South Africa in UAE, 2024', 7572: 'ICC Cricket World Cup League Two 2023-27'}

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
        self.display_series(self.internation_series_names_live)
        self.live_canvas.place(x=50, y=150)

        self.series_var = tkinter.StringVar()
        self.series_id = tkinter.Entry(self.live_canvas, textvariable= self.series_var, font= ('arial', 20, 'bold'))
        self.series_id.place(x=250, y=500)

        self.live_submit = tkinter.Button(self.live_canvas, text= "Show", font= ('arial', 20, 'bold'), foreground= "black",
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
        self.ranking_button = tkinter.Button(self.ranking_canvas, text= "Ranking", font= ('arial', 20, 'bold'),
                                             command= self.get_ranking)
        self.ranking_button.place(x=100, y=170)

        self.ranking_canvas.place(x= 850, y=150)

    def check_series(self):

        id = int(self.series_id.get())

        series_found = False
        if id in self.internation_series_names_live.keys():
            series_found = True
            print(f"Match Found {id}: {self.internation_series_names_live[id]}")
        else:
            print("Please check and try again")

        if series_found:
            # create a new window named after the series name.
            self.series_window = tkinter.Toplevel()
            self.series_window.title(f"{self.internation_series_names_live[id]}")
            self.series_window.geometry("1200x800")
            self.series_window.config(bg="lavender")

            # get series data and assign the values to series data variable.
            key_id =  os.getenv('rapid_api_key')
            key_host = os.getenv('radip_api_host')
            end_point_url = os.getenv('end_point_series')
            self.series_data = self.cric_obj.get_series_data(url=end_point_url, key=key_id, host=key_host, series_id=id)

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

    def get_ranking(self):
        format_type = self.format_type.get()
        format_category = self.category_type.get()
        self.ranking_data = self.cric_obj.get_ranking(format_type, format_category)
        self.display_ranking()

    def display_ranking(self):

        # delete canvas.
        self.ranking_canvas.delete("ranking")

        if self.ranking_data is not None:
            x_ = 20
            y_ = 250
            for num in range(10):
                rank = num + 1
                name = self.ranking_data["response"]['rank'][num]['name']
                country = self.ranking_data["response"]['rank'][num]['country']
                rating = self.ranking_data["response"]['rank'][num]['rating']

                text = f"{rank}: {name},{country}"
                self.ranking_canvas.create_text(x_, y_, text= text, font= ('arial', 15, 'bold'), fill= "black",
                                                tags="ranking", anchor='w')
                y_ += 30


app = UserInterface()
app.exit()