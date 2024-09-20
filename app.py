import os
import tkinter

from dotenv import load_dotenv
from fetch_data import Fetch_Data


class UserInterface:

    load_dotenv()

    def __init__(self):

        self.cric_obj = Fetch_Data(os.getenv('rapid_api_key'), os.getenv('radip_api_host'), os.getenv('end_point_cricketbuzz'))

        self.window = tkinter.Tk()
        self.window.title("Cricket Buzz")
        self.window.geometry("1000x800")
        self.window.config(bg="lavender")

    def exit(self):
        self.window.mainloop()

app = UserInterface()
app.exit()