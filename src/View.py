import customtkinter

from src.ui import TasksFrame

from src.new_ui import SidebarFrame

class View(customtkinter.CTk):
    def __init__(self, ):
        super().__init__()
        self.geometry("600x500")
        self.title("CTk example")

        self.mf = SidebarFrame.Sidebar(self)


        ## self.upd_btn = customtkinter.CTkButton(self, text='update')
        ## self.upd_btn.pack(pady=10, padx=30)

        ## self.child_win_btn = customtkinter.CTkButton(self, text='create task')
        ## self.child_win_btn.pack(pady=10, padx=30)

        ## self.tasks_frame = TasksFrame.TasksFrame(self)
        ## self.tasks_frame.pack()






