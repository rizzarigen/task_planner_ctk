from src.Controller import Controller
from src.model import Model
from src.View import View

if __name__ == "__main__":
    app = Controller(model=Model.Model(), view=View())
    app.start()

