import customtkinter

from src.ui import TasksFrame

class View(customtkinter.CTk):
    def __init__(self, ):
        super().__init__()
        self.geometry("600x500")
        self.title("CTk example")
        self.grid_columnconfigure(2, weight=10)


        self.upd_btn = customtkinter.CTkButton(self, text='update')
        self.upd_btn.grid(row=1, column=1, pady=10, padx=30)

        self.child_win_btn = customtkinter.CTkButton(self, text='create task')
        self.child_win_btn.grid(row=2, column=1, pady=10, padx=30)

        self.tasks_frame = TasksFrame.TasksFrame(self)
        self.tasks_frame.grid(row=0, column=1, pady=10, padx=20, columnspan=2)






