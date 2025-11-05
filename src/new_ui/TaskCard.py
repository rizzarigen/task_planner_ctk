from customtkinter import CTkFrame, CTkLabel, CTkButton
from src.model import Task
from src import Controller



DPI_SCALING = 1

class TaskCard(CTkFrame):
    def __init__(self, master, controller: Controller, task: Task, id, dpi_scale:int , **kwargs) -> None:
        super().__init__(master, border_width=4, **kwargs)

        # add widgets onto the frame, for example:
        self.title = CTkLabel(self, text = task.title, font=("Segoe UI", 20))
        self.description = CTkLabel(self, text = task.description, font=("Segoe UI", 12))
        self.controller = controller
        self.__id = id

        self.startX = task.x
        self.startY = task.y

        self.del_btn = CTkButton(self, text="delete task", command= lambda: controller.delete_task(self.__id, self))

        self.title.pack(pady=9, padx=25)
        self.description.pack(pady=7, padx=25)
        self.del_btn.pack(pady=7, padx=25)

        self.bind("<Button-1>", self.drag_start)
        self.bind("<B1-Motion>", self.drag_motion)

        self.DPI_SCALING = dpi_scale
        self.task = task

    def drag_start(self, event):
        
        self.startX = (event.x) / self.DPI_SCALING
        self.startY = (event.y) / self.DPI_SCALING
        self.lift()

    def drag_motion(self, event):
        x = (event.x + self.winfo_x()) / self.DPI_SCALING - self.startX
        y = (event.y + self.winfo_y()) / self.DPI_SCALING - self.startY
        self.place(x=x,y=y)
        self.task.x = x
        self.task.y = y

        self.controller._model.save_tasks_into_file()

