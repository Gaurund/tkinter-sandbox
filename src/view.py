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
        self.button_blank = ttk.Button(self.main_frame, text="Clean", command=self.clear_frame_right)
        self.button_show = ttk.Button(self.main_frame, text="Show")

        self.frame_right = ttk.Frame(self.main_frame)

        self.button_increase.grid(column=0, row=0)
        self.button_decrease.grid(column=0, row=1)
        self.button_blank.grid(column=0, row=2)
        self.button_show.grid(column=0, row=3)
        self.frame_right.grid(column=1, row=0, rowspan=4)

        self.display_counter()

    def setup_callbacks(self, commands):
        self.button_increase.config(command=commands["increase"])
        self.button_decrease.config(command=commands["decrease"])
        self.button_show.config(command=commands["show"])

    def clear_frame_right(self):
        self.clear_frame(self.frame_right)

    def display_counter(self):
        self.label_counter = ttk.Label(self.frame_right, textvariable=self.label_text)
        self.label_counter.grid(column=0, row=0)

    def change_counter(self, counter):
        self.clear_frame_right()
        self.display_counter()
        self.label_text.set(counter)

    def clear_frame(self, frame: ttk.Frame):
        for child in frame.winfo_children():
            child.destroy()

    def show(self, text: str):
        self.clear_frame_right()
        self.to_show = StringVar()
        self.to_show.set(text)
        self.label_show_text = ttk.Label(self.frame_right, textvariable=self.to_show)
        self.label_show_text.grid(column=0, row=0)