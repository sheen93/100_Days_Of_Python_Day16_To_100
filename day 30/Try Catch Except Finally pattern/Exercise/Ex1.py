fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    if index > (len(fruits)-1):
        raise IndexError("Fruit pie")
    else:
        fruit = fruits[index]
        print(fruit + " pie")

make_pie(5)