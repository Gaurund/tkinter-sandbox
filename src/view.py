from tkinter import Tk, ttk, StringVar

class View:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Testing MVC")
        self.root.geometry("600x400")

        self.main_frame = ttk.Frame(self.root)
        self.main_frame.grid(column=0, row=0)

        self.label_text = StringVar()
        self.label_text.set("0")
        self.button_increase = ttk.Button(self.main_frame, text="Increase")
        self.button_decrease = ttk.Button(self.main_frame, text="Decrease")
        self.label_counter = ttk.Label(self.main_frame, textvariable=self.label_text)

        self.button_increase.grid(column=0,row=0)
        self.button_decrease.grid(column=0,row=1)
        self.label_counter.grid(column=1,row=0)
    
    def setup_callbacks(self, commands):
        self.button_increase.config(command=commands["increase"])
        self.button_decrease.config(command=commands["decrease"])

    def display_counter(self, counter):
        self.label_text.set(counter)
