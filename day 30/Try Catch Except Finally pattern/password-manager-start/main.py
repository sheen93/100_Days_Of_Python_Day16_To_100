import email
from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json

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
    new_data = {
        website: {
            "email/user": user_email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Important field is empty!")
    else:
        is_ok = messagebox.showinfo(title=website, message=f"Email/User: {user_email}\n"
                                                      f"Password: {password}")
        if is_ok:
            try:
                # Reading old data
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                # If file doesn't exist, start with the new_data
                data = new_data
            else:
                # updating old data with new data
                data.update(new_data)
            finally:
                # saving updated data
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    master_pass = "0000"

    # verify = messagebox.askquestion("Security Check", "Are you an authorized user?")

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            user_email = data[website]["email/user"]
            password = data[website]["password"]
            if user_email == user_entry.get():
                messagebox.showinfo(title=website, message=f"Email/User: {user_email}\n"
                                                       f"Password: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No data found for the website under user/email: {user_entry.get()}")
        else:
            messagebox.showinfo(title="Error", message=f"No data found for {website}")

def open_search_window():
    search_window = Toplevel(window)
    search_window.title("Secure Vault Search")
    search_window.config(padx=20, pady=20)
    search_window.grab_set()

    Label(search_window, text="Enter Master Password: ").grid(column=0, row=0)
    master_entry = Entry(search_window, show="*")
    master_entry.grid(column=1, row=0)
    search_window.focus = master_entry

    def verify_and_search():
        if master_entry.get() == "0000":
            search_window.destroy()
            find_password()
        else:
            messagebox.showerror("Denied", "Incorrect Master Password")

    search_window.bind("<Return>", lambda event: (verify_and_search()))
    Button(search_window, text="Unlock & Search", command=verify_and_search).grid(column=1,row=1)

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
add_button.grid(column=1, row=4, columnspan=1, sticky="EW")

search_button = Button(text="Search Password", command=open_search_window)
search_button.grid(column=2, row=4, columnspan=1, sticky="EW")


window.mainloop()