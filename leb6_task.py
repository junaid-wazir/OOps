class Engine:
    def run(self):
        print("Engine is started.")

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        self.__engine = Engine()

    def start(self):
        self.__engine.run()
        print(f"{self.__brand} {self.__model} is starting.")

car1 = Car("Toyota", 2027)
car1.start()        
