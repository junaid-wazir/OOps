class Robot:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def greet(self):
        return f"Hello, I am {self.name}, model {self.color}."


class Robot2:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def __str__(self):
        return f"Hello, I am {self.name}, model {self.model}."

robo=Robot("RoboX", "Red")
robo.greet()
robo2=Robot2("RoboY", "X200")
print(robo2)