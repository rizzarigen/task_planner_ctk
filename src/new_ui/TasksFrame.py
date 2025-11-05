from customtkinter import *
from src.new_ui import TaskCard

class TasksFrame(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        self.master = master
        super().__init__(self.master, **kwargs)

        self.pack(expand=True, fill="both", side="right")

    def m3_click(self, event):


        print(self.startX)
        print(self.startY)
    

