numbers = [1,2,3,4,5,6,7,8,9]

new_numbers = [n+1 for n in numbers]

print(new_numbers)

range_list = [n * 2 for n in range(1, 5)]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "freddie"]

short_name = [short_names for short_names in names if len(short_names)<=4 ]

upper_long_names = [name.upper() for name in names if len(name)>=5]
print(upper_long_names)
