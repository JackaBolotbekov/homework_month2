"""ДЗ"""  # добавил параметр "name" что бы было логичнее
from ftplib import print_line


class Person:
    # инициализатор
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        edu_text = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(
            f"Привет! Меня зовут {self.name}, и моя - дата рождения: {self.birth_date}, профессия: {self.occupation} и у меня {edu_text}")


# два класса-наследника:
class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        edu_text = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}. Я одногрупник Жайыла из группы «{self.group_name}». "
              f"Родился {self.birth_date}, работаю {self.occupation}, у меня {edu_text}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        # добавляем к базовому представлению информацию о хобби
        edu_text = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}. Я друг Жайыла и увлекаюсь: {self.hobby}. "
              f"Родился {self.birth_date}, работаю {self.occupation}, у меня {edu_text}.")


bayel_person = Person("Жайыл", 07.02, "андроид-разработчик", True)
bayel_person.introduce()

# одноклассники - одногрупники
classmate1 = Classmate(
    name="Нурбол",
    birth_date="05.12.2009",
    occupation="программистом",
    higher_education=True,
    group_name="B-59-1"
)
classmate2 = Classmate(
    name="Элдияр",
    birth_date="16.02.2009",
    occupation="backend'щиком",
    higher_education=True,
    group_name="B-59-1"
)

# друзья
friend1 = Friend(
    name="Илья",
    birth_date="05.12.2005",
    occupation="доставщиком",
    higher_education=True,
    hobby="мотики"
)
friend2 = Friend(
    name="Рамазан",
    birth_date="13.07.2006",
    occupation="работником в call-центре",
    higher_education=False,
    hobby="машины"
)

classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()

# DOP - 1
list_objects = (classmate1, classmate2, friend1, friend2)
for i in list_objects:
    i.introduce()

# либо так
people = [
    Person("Султан", "30.12.2000", "data-scientist", True),
    Classmate("Бектур", "05.12.2000", "программист", False, "PY-23"),
    Friend("Алмаз", "05.12.2000", "программист", True, "футбол"),
    Friend("Байэл", "13.07.2001", "дизайнер", False, "фото и монтаж"),
    Classmate("Айбек", "16.02.2001", "аналитик", True, "PY-23"),
]

for person in people:
    person.introduce()


# DOP - 2
class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, shared_memory):
        super().__init__(name, birth_date, occupation, higher_education, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        super().introduce()
        print_line(f"Наше общее воспоминание: {self.shared_memory}.")


best_friend = BestFriend(
    name="Талгат",
    birth_date="06.10.2007",
    occupation="frontend - разработчиком",
    higher_education=False,
    hobby="anime",
    shared_memory="сидели до рассвета, писали первый бот"
)
best_friend.introduce()

"""код с урока"""
# # родитель, суперкласс
# class Car:
#     # инициализатор
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
#     def drive_to_location(self, location):
#         print(f"Car {self.model} is driving to {location}")
#
# # дочерний класс, наследник
# class Bus(Car):
#     def __init__(self, model, color, seats):
#         super().__init__(model, color)
#         self.seats = seats
#
#     def drive_to_location(self, location):
#         # super().drive_to_location(location)
#         print(f"Bus {self.model} is driving to {location}")
#
#     def test_bus(self):
#         print(f"Bus test bus {self.color}")
#
# class Truck(Car):
#     pass
#
#
# bus_1 = Bus(model="Mercedes", color="green", seats=30)
# print(bus_1.model)
# print(bus_1.seats)
# bus_1.drive_to_location("Bishkek")
# bus_1.test_bus()
#
# print(type(bus_1))
# print(isinstance(bus_1, Bus))
# print(isinstance(bus_1, Car))
# print(isinstance(bus_1, Truck))
