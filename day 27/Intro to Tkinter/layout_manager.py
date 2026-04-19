from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = text_input.get()
    my_label.config(text=new_text)

#window
window = Tk()
window.title("Layout Manager")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

#label
my_label = Label(text="New Text", font=("Arial", 24, "bold"))
my_label.grid(column=0,row=0)
my_label.config(padx=50, pady=50)

#button
button = Button(text="Click the button", command=button_clicked)
button.grid(column=1,row=1)

#button2
button2 = Button(text="Click me 2")
button2.grid(column=2,row=0)

#entry
text_input = Entry(width=10)
print(text_input.get())
text_input.grid(column=3,row=2)


window.mainloop()