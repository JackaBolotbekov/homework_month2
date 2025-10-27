from lessons.lesson_1 import Car

# dunder methods double underscore
class Money:
    def __init__(self, amount=0):
        self.amount = amount

    def __str__(self):
        return f"Money obj amount={self.amount}"

    def __eq__(self, other):
        if self.amount == other.amount:
            return True
        return False

    # gt - greater than: >
    # ge - greater than or equal: >=
    # lt - less than: <
    # le - less than or equal: <=
    def __gt__(self, other):
        if self.amount > other.amount:
            return True
        return False

    def __add__(self, other):
        new_money = Money(amount=self.amount + other.amount)
        return new_money

    # subtraction
    def __sub__(self, other):
        new_money = Money(amount=self.amount - other.amount)
        return new_money

money_igor = Money(amount=1000)
money_mirlan = Money(amount=2000)
print(money_igor)
print(money_mirlan)

print(money_igor == money_mirlan)
print(money_igor > money_mirlan)
print(money_mirlan > money_igor)

print(f"Add two money objs: {money_igor + money_mirlan}")


car_1 = Car(model='Honda', color='White')
print(car_1)