from customtkinter import *

class CreatorFrame(CTkFrame):
        def __init__(self, master, *args, **kwargs):
            super().__init__(master, **kwargs)

            self.__master = master


            self.title_entry = CTkEntry(master=self, placeholder_text="title")
            self.desc_entry = CTkEntry(master=self, placeholder_text="description")
            self.confirm_btn = CTkButton(self, text='Confirm')

            self.visibility_btn = CTkButton(self, text="X", fg_color="red", width=20, height=20, command=self.hide)

            self.visibility_btn.pack(anchor="nw", side="top", padx=3, pady=5)
            
            self.title_entry.pack(side="top", pady=5, padx=7)
            self.desc_entry.pack(side="top", pady=5, padx=7)
            self.confirm_btn.pack(side="top", pady=15, padx=7)

            
            self.pack(side="bottom", fill="x", pady=15, padx=15)

        def hide(self):
            self.destroy()



            