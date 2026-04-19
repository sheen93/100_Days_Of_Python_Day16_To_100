#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

guest_list = []
with open("Input/Names/invited_names.txt", mode="r") as name_file:
    for name in name_file.readlines():
        guest_list.append(name)
print(guest_list)

# letter = open("Input/Letters/starting_letter.txt")
# letter_content = letter.read()
#
# for guest in guest_list:
#     guest_name = guest.strip("\n")
#     with open(f"Output/ReadyToSend/letter_for_{guest_name}.txt", mode="w+") as new_letter:
#         new_content = letter_content.replace("[name]", guest_name)
#         new_letter.write(new_content)
#
# letter.close()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for guest in guest_list:
        guest_name = guest.strip()
        new_letter = letter_content.replace("[name]", guest_name)
        with open(f"Output/ReadyToSend/letter_for_{guest_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)