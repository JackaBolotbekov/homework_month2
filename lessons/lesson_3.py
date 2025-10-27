# родитель, суперкласс
class Car:
    # инициализатор
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def drive_to_location(self, location):
        print(f"Car {self.model} is driving to {location}")

# дочерний класс, наследник
class Bus(Car):
    def __init__(self, model, color, seats):
        super().__init__(model, color)
        self.seats = seats

    def drive_to_location(self, location):
        # super().drive_to_location(location)
        print(f"Bus {self.model} is driving to {location}")

    def test_bus(self):
        print(f"Bus test bus {self.color}")

class Truck(Car):
    pass


car_honda = Car(model='Honda', color='White')
bus_1 = Bus(model="Mercedes", color="green", seats=30)
bus_1.drive_to_location(location="Bishkek")
car_honda.drive_to_location(location="Karakol")

vehicles = [car_honda, bus_1]

for v in vehicles:
    v.drive_to_location(location="Bishkek")