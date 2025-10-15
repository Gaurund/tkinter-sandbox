from src.model import Model
from src.view import View


class Controller:
    def __init__(self, view: View, model: Model) -> None:
        self.view = view
        self.model = model

        self.view.setup_callbacks(
            {"increase": self.increase, "decrease": self.decrease}
        )

    def increase(self):
        self.model.increase()
        self.display()

    def decrease(self):
        self.model.decrease()
        self.display()

    def display(self):
        counter = self.model.counter
        self.view.display_counter(counter=counter)
