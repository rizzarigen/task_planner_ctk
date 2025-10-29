from src.Controller import Controller
from src.model import Model
from src.View import View
from src.ui import TaskCard

if __name__ == "__main__":
    app = Controller(model=Model.Model(), view=View())
    app.start()

