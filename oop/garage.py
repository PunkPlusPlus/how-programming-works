class Car:
    color: str
    max_speed: float
    year_of_issue: int

    def __init__(self, color, max_speed, year_of_issue):
        self.color = color
        self.max_speed = max_speed
        self.year_of_issue = year_of_issue

class Garage:
    cars = []

    def add(self, car: Car):
        self.cars.append(car)

    def __len__(self):
        return len(self.cars)


car1 = Car('black', 150, 1997)
car2= Car('white', 200, 2004)

garage = Garage()


garage.add(car1)
garage.add(car2)

print(len(garage))



