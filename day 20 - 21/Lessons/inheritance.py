class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Inhale ...... Exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Moving under water")

    def breathe(self):
        super().breathe()
        print("doing under water")