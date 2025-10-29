from customtkinter import CTkFrame

class TasksFrame(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, width=600, height=600, **kwargs)
