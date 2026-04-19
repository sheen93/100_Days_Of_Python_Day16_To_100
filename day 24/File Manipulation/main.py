#Basic file open method
file = open("text_file.txt")
content = file.read()
print(content)
file.close() #if file is not closed manually, it would stay open

#Advanced - excuses the need to close file manually
with open("text_file.txt", mode="r") as f:
    contents = f.read()
    print(contents)

with open("new_file.txt", mode="w") as f: #mode="w", deletes the contents inside the file and rewrites it with new content, but doesn't allow to read and moves pointer at the beginning
    f.write("New file! New text!") #opens a new file in the same directory if the file name does not exist

with open("new_file.txt", mode="a+") as f: #mode="a+", adds content inside the file at the end, allows to read and moves pointer at the end
    f.write("\nAdding this new text to the file")
    f.seek(0) #brings pointer back to beginning
    new_content = f.read()
    print(new_content)

