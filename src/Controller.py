from asyncio import create_task

from src.model import Model
from src import View
import customtkinter
from src.new_ui import TaskCard


from src.model.Task import Task

from src.new_ui import SidebarFrame

import ctypes


def get_windows_dpi():
    hdc = ctypes.windll.user32.GetDC(0)
    dpi = ctypes.windll.gdi32.GetDeviceCaps(hdc, 88)  # 88: LOGPIXELSX
    ctypes.windll.user32.ReleaseDC(0, hdc)
    return dpi

class Controller:
    def __init__(self, model: Model.Model, view: View.View):
        self._model = model
        self._view = view

        self.update_view()

        self.mf = SidebarFrame.Sidebar(master=self._view, controller=self)
        self.DPI_SCALING = dpi_scale=get_windows_dpi() / 96
        

        ## self._task_creator_window = None

        ## self._view.child_win_btn.configure(command=self.open_creator_window)
        ## self._view.upd_btn.configure(command=self.update_view)


        



    def draw_tasks(self, tasks: dict):
        for widget in self._view.tasks_frame.winfo_children():
            widget.destroy()
            
        

        if len(tasks) != 0:
            for task_id in tasks:
                card = TaskCard.TaskCard(self._view.tasks_frame, self, tasks[task_id], task_id, dpi_scale= get_windows_dpi() / 96 )
                card.place(x=tasks[task_id].x, y=tasks[task_id].y )
        else:
            empty_card = TaskCard.TaskCard(self._view.tasks_frame, self, Task(), 0, dpi_scale=get_windows_dpi() / 96)
            empty_card.del_btn.destroy()
            empty_card.place(x=50, y=100)



    def update_view(self):
        self._view.update()
        self._model.update_tasks_from_file()
        self.draw_tasks(tasks=self._model.tasks)

    def create_task(self):
        new_task = Task(title = self.mf.creator_frame.title_entry.get(),
                        description=self.mf.creator_frame.desc_entry.get(),
                        priority=1)
        self._model.add_task(new_task)
        self._model.save_tasks_into_file()
        self.update_view()
        pass

    def delete_task(self, task_id, card: TaskCard.TaskCard):
    
        card.grid_forget()
        card.destroy()
        self._model.delete_task(task_id)
        self._model.save_tasks_into_file()
        self.update_view()



    def start(self):
        self._view.mainloop()
