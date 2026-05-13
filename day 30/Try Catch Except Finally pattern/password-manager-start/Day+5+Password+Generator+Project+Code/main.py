#Password Generator Project
import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = "!#$%&()*+"

password_list = [str(random.choice(letters)) for _ in range(random.randint(8, 10))]
password_list += [str(random.choice(numbers)) for _ in range(random.randint(2, 4))]
password_list += [str(random.choice(symbols)) for _ in range(random.randint(2, 4))]

random.shuffle(password_list)
password = "".join(password_list)
print(f"Password generated: {password}")