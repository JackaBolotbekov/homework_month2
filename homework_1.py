"""ДЗ"""


class Person:
    # инициализатор
    def __init__(self, birth_date, occupation, higher_education):
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education


sultan_student = Person(12.30, "data-since", True)
meder_student = Person(07.13, "businessmen", False)
zhayil_student = Person(02.16, "android-developer", False)

print(
    f"Sultan - birth date: {sultan_student.birth_date}, occupation: {sultan_student.occupation}, higher education: {sultan_student.higher_education}")
print(
    f"Meder - birth date: {meder_student.birth_date}, occupation: {meder_student.occupation}, higher education: {meder_student.higher_education}")
print(
    f"Zhayil - birth date: {zhayil_student.birth_date}, occupation: {zhayil_student.occupation}, higher education: {zhayil_student.higher_education}")

"""код с урока"""
# class Car:
#     # инициализатор
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
#     def drive_to_location(self, location):
#         print(f"Car {self.model} is driving to {location}")
#
# # создание объектов
# car_honda = Car(model='Honda', color='White')
# car_subaru = Car(color='Red', model='Subaru')
#
# print(car_honda)
# print(f"Car model: {car_honda.model}, color: {car_honda.color}")
# print(car_subaru)
# print(f"Car model: {car_subaru.model}, color: {car_subaru.color}")
#
# car_honda.drive_to_location("Karakol")
#
# print(type("aaaaaaaaa"))
# print(type(123123))
# print(type(car_honda))
