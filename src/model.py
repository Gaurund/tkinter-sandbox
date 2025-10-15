class Model:
    def __init__(self) -> None:
        self.counter = 0

    def increase(self):
        self.counter += 1

    def decrease(self):
        self.counter -= 1
