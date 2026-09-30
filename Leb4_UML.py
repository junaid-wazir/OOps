class Robot:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def greet(self):
        return f"Hello, I am {self.name}, model {self.color}."

robo=Robot("RoboX", "Red")
robo.greet()