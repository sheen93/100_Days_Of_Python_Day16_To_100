"""Unlimited positional arguments"""
def add(*args):
    """ '*' gives the option for unlimited positional arguments in the method. after *, it could be any name but commonly used *args"""
    print(args)
    """Returns a tuple object"""
    for n in args: #looping through tuple
        print(n)


add(3,9,5)


"""Unlimited keyword arguments"""
def calculate(n, **kwargs):
    """ '**' gives the option for unlimited keyword arguments in the method. after **, it could be any name but commonly used *kwargs"""
    print(kwargs)
    """Returns a dictionary object"""
    print(kwargs["add"])
    for key, value in kwargs.items(): #looping through dictionary
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
