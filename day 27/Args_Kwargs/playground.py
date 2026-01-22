def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(5,6,8,7,10))

"""Unlimited keyword arguments"""
def calculate(n, **kwargs):
    n += kwargs["add"] # adds the "add" key argument value to n
    n *= kwargs["multiply"] # multiplies the "multiply" key argument value to n
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        """" ".get()" allows the method to create an object even if all the attributes are not defined while creating the object. returns None if not specified"""
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.color = kw.get("seats")

my_car = Car(make="Infiniti", model= "G35s")

print(my_car.make)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)