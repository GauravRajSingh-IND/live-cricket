import tkinter


class UserInterface:

    def __init__(self):

        self.window = tkinter.Tk()
        self.window.title("Cricket Buzz")
        self.window.geometry("1000x800")

    def exit(self):
        self.window.mainloop()

app = UserInterface()
app.exit()