from customtkinter import CTkFrame, CTkLabel, CTkButton
from src.model import Task
from src import Controller



DPI_SCALING = 1

class TaskCard(CTkFrame):
    def __init__(self, master, controller: Controller, task: Task, id, dpi_scale:int , **kwargs) -> None:
        super().__init__(master, fg_color="red", **kwargs)

        # add widgets onto the frame, for example:
        self.title = CTkLabel(self, text = task.title, font=("Segoe UI", 20))
        self.description = CTkLabel(self, text = task.description, font=("Segoe UI", 12))
        self.controller = controller
        self.__id = id

        self.startX = task.x
        self.startY = task.y

        self.del_btn = CTkButton(self, text="delete task", command= lambda: controller.delete_task(self.__id, self))

        self.title.grid(row=0, column=0, padx=20)
        self.description.grid(row=1, column=0)
        self.del_btn.grid(row=2, padx=20, pady=7)

        self.bind("<Button-1>", self.drag_start)
        self.bind("<B1-Motion>", self.drag_motion)

        self.DPI_SCALING = dpi_scale
        self.__task = task

    def drag_start(self, event):
        
        self.startX = (event.x) / self.DPI_SCALING
        self.startY = (event.y) / self.DPI_SCALING

    def drag_motion(self, event):
        x = (event.x + self.winfo_x()) / self.DPI_SCALING - self.startX
        y = (event.y + self.winfo_y()) / self.DPI_SCALING - self.startY
        self.place(x=x,y=y)
        self.__task.x = x
        self.__task.y = y

        print(self.__task.x)
        print(self.__task.y)
        self.controller._model.save_tasks_into_file()

