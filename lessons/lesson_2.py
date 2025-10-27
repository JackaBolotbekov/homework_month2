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


bus_1 = Bus(model="Mercedes", color="green", seats=30)
print(bus_1.model)
print(bus_1.seats)
bus_1.drive_to_location("Bishkek")
bus_1.test_bus()

print(type(bus_1))
print(isinstance(bus_1, Bus))
print(isinstance(bus_1, Car))
print(isinstance(bus_1, Truck))
