from tkinter import *


# Checks if new input is a valid number; linked via validatecommand
def validate_input(new_text):
    if not new_text: return True  # Allow backspacing all characters
    try:
        float(new_text)
        return True
    except ValueError:
        return False


# Main conversion logic; handles both Button clicks and Key events
def convert(event=None):
    # window.focus_get() ensures we convert based on the active input field
    if window.focus_get() == mile_convert:
        miles_text = mile_convert.get()
        if miles_text:
            kms = round(float(miles_text) * 1.60934, 2)
            km_convert.delete(0, END)  # Clear existing value before update
            km_convert.insert(0, string=f"{kms}")

    elif window.focus_get() == km_convert:
        km_text = km_convert.get()
        if km_text:
            miles = round(float(km_text) * 0.621371, 2)
            mile_convert.delete(0, END)  # Clear existing value before update
            mile_convert.insert(0, string=f"{miles}")


# Clears both entry widgets; used by Reset Button and Delete key
def reset():
    mile_convert.delete(0, END)
    km_convert.delete(0, END)


# UI Setup
window = Tk()
window.title("Miles to Km Converter")
window.config(padx=50, pady=30)

# Global Key Bindings
window.bind("<Return>", lambda event: convert())
window.bind("<Delete>", lambda event: reset())

# Register validation function for use by Tcl/Tk engine
vcmd = window.register(validate_input)

# Mile UI Elements
mile = Label(text="Mile(s):", font=("Arial", 12, "bold"))
mile.grid(column=1, row=1)

mile_convert = Entry(width=10)
mile_convert.grid(column=2, row=1)
# Auto-clear the opposite box when user clicks here to start a new conversion
mile_convert.bind("<FocusIn>", lambda event: km_convert.delete(0, END))
# Real-time restriction: validate="key" checks input BEFORE it appears using %P
mile_convert.config(validate="key", validatecommand=(vcmd, '%P'))

# Km UI Elements
km = Label(text="Km(s):", font=("Arial", 12, "bold"))
km.grid(column=1, row=2)

km_convert = Entry(width=10)
km_convert.grid(column=2, row=2)
# Auto-clear the opposite box when user clicks here
km_convert.bind("<FocusIn>", lambda event: mile_convert.delete(0, END))
km_convert.config(validate="key", validatecommand=(vcmd, '%P'))

# Action Buttons
convert_button = Button(text="Convert (Enter)", command=convert)
convert_button.grid(column=2, row=3)

reset_button = Button(text="Reset (Delete)", command=reset)
reset_button.grid(column=2, row=4)

window.mainloop()
