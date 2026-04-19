from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!#$%&()*+"

    password_list = [str(random.choice(letters)) for _ in range(random.randint(8, 10))]
    password_list += [str(random.choice(numbers)) for _ in range(random.randint(2, 4))]
    password_list += [str(random.choice(symbols)) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_entry.get()
    password = password_entry.get()
    user_email = user_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Important field is empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {user_email}\n"
                                                      f"Password: {password}")
        if is_ok:
            with open("data.txt", mode="a") as f:
                f.seek(0)
                f.write(f"Website: {website}\n"
                        f"User/Email: {user_email}\n"
                        f"Password: {password}\n"
                        f"-------------------------------------------\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

lock_img = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1, row=0)

#labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entry
website_entry = Entry()
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

user_entry = Entry()
user_entry.insert(0, "msheen.ameen@gmail.com")
user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

#button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", command=save_pass)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()