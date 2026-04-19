with open("../../new_file.txt") as f:
    content = f.read()
    print(content)

with open("/Users/mshee/Desktop/Python2/day 24/File Manipulation/newest_file.txt", mode="w+") as file:
    new_content = file.write("This is a new file created from a different directory using python's internal coding")
    print(file.read())