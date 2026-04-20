
"""---------------------------ERRORS-----------------------------"""
#FileNotFound
# with open("a_file.txt") as file:
#     file.read()
try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["ke"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")


#KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent"]

#IndexError
# fruit_list = ["Apple", "Banana", "Orange"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)
