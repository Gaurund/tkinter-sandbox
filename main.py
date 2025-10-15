from tkinter import Tk

from src.controller import Controller
from src.model import Model
from src.view import View

model = Model()
root = Tk()
view = View(root=root)
controller = Controller(view, model)
root.mainloop()