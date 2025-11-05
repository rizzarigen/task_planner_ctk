from customtkinter import *

class MainFrame(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        self.master = master
        super().__init__(self.master, **kwargs)
        self.pack()
        print(self.winfo_width(), self.winfo_height())

        self.upBtn = CTkButton(self, text='Up')
        self.upBtn.pack(pady=7, padx=15)

        self.downBtn = CTkButton(self, text='Down')
        self.downBtn.pack(pady=7, padx=15)