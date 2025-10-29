from customtkinter import CTkScrollableFrame

class TasksFrame(CTkScrollableFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, orientation='horizontal', width=600, **kwargs)
        self.grid_rowconfigure(0, weight=5)
