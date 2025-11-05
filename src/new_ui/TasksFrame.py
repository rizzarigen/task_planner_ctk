from customtkinter import *

class TasksFrame(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        self.master = master
        super().__init__(self.master, **kwargs)

        self.pack(expand=True, fill="both", side="right")