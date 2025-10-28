from customtkinter import CTkFrame, CTkLabel, CTkButton
from src.model import Task
from src import Controller

class TaskCard(CTkFrame):
    def __init__(self, master, controller: Controller, task: Task, id , **kwargs) -> None:
        super().__init__(master, fg_color="red", **kwargs)

        # add widgets onto the frame, for example:
        self.title = CTkLabel(self, text = task.title, font=("Segoe UI", 20))
        self.description = CTkLabel(self, text = task.description, font=("Segoe UI", 12))
        self.controller = controller
        self.__id = id

        self.del_btn = CTkButton(self, text="delete task", command= lambda: controller.delete_task(self.__id, self))

        self.title.grid(row=0, column=0, padx=20)
        self.description.grid(row=1, column=0)
        self.del_btn.grid(row=2, padx=20, pady=7)

