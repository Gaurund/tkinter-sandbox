from src.model import Model
from src.view import View


class Controller:
    def __init__(self, view: View, model: Model) -> None:
        self.view = view
        self.model = model

        self.view.setup_callbacks(
            {"increase": self.increase, "decrease": self.decrease, "show": self.show}
        )

    def increase(self):
        self.model.increase()
        self.change_counter()

    def decrease(self):
        self.model.decrease()
        self.change_counter()

    def change_counter(self):
        counter = self.model.counter
        self.view.change_counter(counter=counter)

    def show(self):
        text = """Вы можете очистить содержимое фрейма (Frame) в Tkinter, 
        удалив все виджеты, которые в нём находятся.
        Для этого обычно используется метод winfo_children(), 
        который возвращает список всех дочерних виджетов фрейма, 
        и затем эти виджеты уничтожаются с помощью метода destroy()."""
        self.view.show(text=text)
