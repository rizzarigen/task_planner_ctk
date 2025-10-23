import customtkinter

class TaskCreatorWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("150x100")
        self.grid_columnconfigure(2, weight=1)

        self.title_entry = customtkinter.CTkEntry(master=self, placeholder_text="title")
        self.desc_entry = customtkinter.CTkEntry(master=self, placeholder_text="description")
        self.confirm_btn = customtkinter.CTkButton(self, text='create a task')
        self.priority_entry = customtkinter.CTkEntry(self, placeholder_text="priority")

        self.confirm_btn.grid(row=4, column=1, sticky='nsew')
        self.desc_entry.grid(row=2, column=1)
        self.title_entry.grid(row=1, column=1, sticky="nsew")
        self.priority_entry.grid(row=3, column=1)