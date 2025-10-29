from src.model import Task
import json

class TaskVault:
    def __init__(self) -> None:
        self.__tasks = {}

    @property
    def tasks(self):
        return self.__tasks

    def add_task(self, task: Task) -> None:
        keys = list(self.__tasks)
        keys.reverse()
        try:
            last_id = keys[0] + 1
        except:
            last_id = 1
        self.__tasks.update([(last_id, task)])

    def delete_task(self, task_id):
        self.__tasks.pop(task_id)
        new_dict = {}
        for i in range(len(self.__tasks)):
            new_dict[i] = self.__tasks[list(self.__tasks)[i]]

    def get_task(self, task_id):
        return self.__tasks.get(task_id)

    def clean(self):
        self.__tasks = {}


class Model(TaskVault):

    def __init__(self):
        super().__init__()
        self.update_tasks_from_file()

    def __call__(self, *args, **kwargs):
        output = {}
        for task_id in self.tasks:
            output[str(task_id)] = self.tasks[task_id]()



        return output


    def update_tasks_from_file(self):
        self.clean()
        with open("./tasks/tasks.json", 'r') as file:
            tasks = json.load(file)
            for task_id in tasks:
                task = tasks[task_id]
                self.add_task(Task.Task(task["title"], task["description"], task["priority"], x=task["x"], y=task["y"]))

    def save_tasks_into_file(self):
        with open("./tasks/tasks.json", "w") as wfile:
            json.dump(self.__call__(), wfile, indent=4)







