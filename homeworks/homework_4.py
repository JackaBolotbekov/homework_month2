# Homework 4 — MRO

class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car starting")

class ElectricCar(Vehicle):
    def start(self):
        # ничего не печатаем, просто продолжаем цепочку
        return super().start()

class Tesla(ElectricCar, Car):
    def start(self):
        super().start()
        print("Tesla ready")

Tesla().start()

# вернусь к ДОП'ам когда сдам все ДЗ