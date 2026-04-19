from tkinter import *

window = Tk()
window.title("MY FIRST GUI PROGRAM")
window.minsize(width=500, height=300)


#Creating Label
my_label = Label(text="I am a label", font=("Courier", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text" #Can be edited like a dictionary item
my_label.config(text = "Newer Text") #Or can use .config() method to edit

#Button
def button_clicked():
    # my_label["text"]=text_input.get()
    new_text = text_input.get()
    my_label.config(text=new_text)
    print(text_input.get())

button = Button(text="Click Me", command=button_clicked) # "command" argument uses only name of the function, so "()" after button_clicked is not needed
button.pack()

#Entry Component

text_input = Entry(width=10)
text_input.pack()








window.mainloop()