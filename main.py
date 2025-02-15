class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started."

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  

    def drive(self):
        return f"{self.brand} car is driving with {self.engine.horsepower} horsepower."


brand = input("Enter car brand: ")
horsepower = int(input("Enter engine horsepower: "))


engine = Engine(horsepower)
car = Car(brand, engine)

print(engine.start())  
print(car.drive())  
