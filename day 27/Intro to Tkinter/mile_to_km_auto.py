from tkinter import *

def auto_convert(*args):
    focused_widget = window.focus_get()
    try:
        if focused_widget == mile_convert:
            m_val = mile_var.get()
            if m_val:
                kms = round(float(m_val) * 1.60934, 2)
                km_var.set(str(kms))
            else:
                km_var.set("")
        elif focused_widget == km_convert:
            km_val = km_var.get()
            if km_val:
                miles = round(float(km_val) * 0.621371, 2)
                mile_var.set(str(miles))
            else:
                mile_var.set("")
    except ValueError:
        pass

window = Tk()
window.title("Miles/Km converter")
window.config(padx=50,pady=30)

mile = Label(text="Mile(s):", font=("Arial", 12, "bold"))
mile.grid(column=1, row=1)
mile_var = StringVar()
mile_convert = Entry(width=10, textvariable=mile_var)
mile_convert.grid(column=2,row=1)
mile_var.trace_add("write", auto_convert)

km = Label(text="Km(s):", font=("Arial", 12, "bold"))
km.grid(column=1,row=2)
km_var = StringVar()
km_convert = Entry(width=10, textvariable=km_var)
km_convert.grid(column=2, row=2)
km_var.trace_add("write", auto_convert)

window.mainloop()