from customtkinter import *

class Sidebar(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, **kwargs)

        self.__master = master

        self.__WIDTH = 60
        self.__extended_width = self.__WIDTH * 3

        self.configure(width=0)

        self.pack(side="left", fill="y")
        self.pack_propagate(flag=False)

        self.extend_btn = CTkButton(master=master, text=">")
        self.extend_btn.configure(width=30, height=30, command=self.extend_menu)

        self.extend_btn.pack(side="top", anchor="w", padx=self.__WIDTH / 4, pady = self.__WIDTH / 4)
        self.master.pack_propagate(flag=False)

        self.canvas_btn = CTkButton(self, text="Canvas")
        self.creator_btn = CTkButton(self, text="Create a Task")

        self.canvas_btn.configure(command=self.extend_menu)
        self.creator_btn.configure(command=self.extend_menu)

        self.canvas_btn.pack(anchor="center", padx=self.__WIDTH / 4, pady = self.__WIDTH / 4, fill="x")
        self.creator_btn.pack(anchor="center", padx=self.__WIDTH / 4, pady = self.__WIDTH / 4, fill="x")

    def extend_animation(self):
        
        current_width = self.winfo_width()

        if not current_width > self.__extended_width:
            self.configure(width=current_width + 10)

            self.after(ms=8, func=self.extend_animation)

    
    def fold_animation(self):
        if self.winfo_width() == 1:
            self.configure(width = 0)
        elif self.winfo_width() > 0:
            self.configure(width = self.winfo_width() - 10)
            self.after(ms=4, func=self.fold_animation)
            
    
    def extend_menu(self):
        
        self.extend_animation()
        self.extend_btn.configure(text="<", command=self.fold_menu)

    def fold_menu(self):
        self.fold_animation()
        self.extend_btn.configure(text=">", command=self.extend_menu)