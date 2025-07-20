import customtkinter as ctk

class UserInterface:
    def __init__(self):
        # Dark theme(dt) colors
        self.dt_bg = "#3A3A42" #2A2D34
        self.dt_widget_bg = "#2C2C3A"

        self.dt_button_text = "#B18BD0"
        self.dt_button_text_hover = "#E5E4E2"
        self.dt_button_hover_bg = "#8E44AD"


        # App config
        self.app = ctk.Ctk()
        self.app.geometry("800x500")
        self.app.title("Password Manager")
        self.app.configure(fg_color=self.dt_bg)

        



