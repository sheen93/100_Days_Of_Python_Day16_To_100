import email
from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Generate Window Creation
    generate_window = Toplevel()
    generate_window.title("Generate Password")
    generate_window.config(padx=50, pady=50)

    # UI Layout
    Label(generate_window, text="Min Char: ").grid(column=1, row=1, columnspan=1, sticky="EW")

    min_scale = Spinbox(
        generate_window,
        from_=8, to=32,
        width=8, justify="center"
    )
    min_scale.delete(0,END)
    min_scale.insert(0,"12")
    min_scale.grid(column=2,row=1, sticky="E")

    num_state = IntVar(value=1)
    Checkbutton(generate_window, text="Numbers", variable=num_state).grid(column=1, row=2, columnspan=1, sticky="EW")
    sym_state = IntVar(value=1)
    Checkbutton(generate_window, text="Symbols", variable=sym_state).grid(column=2, row=2, columnspan=1, sticky="EW")

    def custom_pass(length=None, use_nums=None, use_syms=None):
        if length is None:
            try:
                length = int(min_scale.get())
                use_nums = num_state.get()
                use_syms = sym_state.get()
            except ValueError:
                messagebox.showwarning("Error", "Enter a valid number")
                return

        char_pool = string.ascii_letters
        if use_nums: char_pool += string.digits
        if use_syms: char_pool += "!#$%&()*+"

        password = "".join(random.choice(char_pool) for _ in range(length))

        is_ok = messagebox.askyesno(title="Password Confirmation", message=f"Confirm Password\n"
                                                                      f"Password: {password}")

        if is_ok:
            password_entry.delete(0,END)
            password_entry.insert(0, password)
            pyperclip.copy(password)
            generate_window.destroy()
        else:
            pass

    def quick_random():
        custom_pass(length=16, use_nums=True, use_syms=True)

    Button(generate_window, text="Generate", command=custom_pass).grid(column=1, row=3, columnspan=1, sticky="EW")
    Button(generate_window, text="Random", command=quick_random).grid(column=2, row=3, columnspan=1, sticky="EW")

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
        messagebox.showinfo(title="Error", message="Required field is empty!")
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
                data = {}

            # Check if website already exists
            if website in data:
                # if it's a list, append
                if isinstance(data[website], dict):
                    # if old data, convert to a list
                    data[website] = [data[website]]

                # check if email exists to avoid email duplication
                email_exists = False
                for account in data[website]:
                    if account["email/user"] == user_email:
                        account["password"] = password
                        email_exists = True

                if not email_exists:
                    data[website].append({"email/user": user_email, "password": password})

            else:
                # new entry
                data[website] = [{"email/user": user_email, "password": password}]

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password(search_term):

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
        return

    matches = []
    for site_key in data:
        if search_term.lower() in site_key.lower():
            accounts = data[site_key]
            if isinstance(accounts, dict):
                accounts = [accounts]

            for acc in accounts:
                matches.append(f"Website/App: {site_key}\n"
                               f"User/Email: {acc["email/user"]}\n"
                               f"Password: {acc["password"]}")

    if matches:
        messagebox.showinfo(title="Search Results", message="\n--------------------\n".join(matches))
    else:
        messagebox.showinfo(title="Not Found", message=f"No matches for {search_term}")

    # else:
    #     if website in data:
    #         user_email = data[website]["email/user"]
    #         password = data[website]["password"]
    #         if user_email == user_entry.get():
    #             messagebox.showinfo(title=website, message=f"Email/User: {user_email}\n"
    #                                                    f"Password: {password}")
    #         else:
    #             messagebox.showinfo(title="Error", message=f"No data found for the website under user/email: {user_entry.get()}")
    #     else:
    #         messagebox.showinfo(title="Error", message=f"No data found for {website}")

def open_search_window():
    search_window = Toplevel(window)
    search_window.title("Secure Vault Search")
    search_window.config(padx=20, pady=20)
    search_window.grab_set()

    Label(search_window, text="Website/App: ").grid(column=0, row=0)
    web_entry = Entry(search_window)
    web_entry.grid(column=1, row=0)

    Label(search_window, text="Master Pass: ").grid(column=0, row=1)
    master_entry = Entry(search_window, show="*")
    master_entry.grid(column=1, row=1)

    if website_entry.get() != "":
        web_entry.insert(0,website_entry.get())
        master_entry.focus()
    else:
        web_entry.focus()

    def verify_and_search():
        if master_entry.get() != "0000":
            messagebox.showerror("Denied", "Incorrect Master Password")
        elif web_entry.get() == "":
            messagebox.showerror("Denied", "Required Field Empty (Website/App)")
        else:
            search_window.destroy()
            find_password(website_entry.get())

    search_window.bind("<Return>", lambda event: (verify_and_search()))
    Button(search_window, text="Unlock & Search", command=verify_and_search).grid(column=1,row=2)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

window.bind("<Control-s>", lambda event: open_search_window())
window.bind("<Control-g>", lambda event: generate_password())

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