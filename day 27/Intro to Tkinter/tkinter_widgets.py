from tkinter import *

window = Tk()
window.title("Tkinter Widget Practice")
window.minsize(width=500, height=500)

#button
def action():
    label.config(text="This is the new text")

button1 = Button(text="Click Me", command=action)
button1.pack()

def action2():
    label.config(text=entry.get())
button2 = Button(text="Click me to change label from entry", command=action2)
button2.pack()



#label
label = Label(text="This is the old text")
label.pack()



#entries
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with")
print(entry.get())
entry.pack()

#text
text = Text(height=5, width=50)
text.focus() #puts cursor on the textbox
text.insert(END, "Example of multiline text entry\n"
                 "And this is the second line")
print(text.get("1.0","1.0 lineend")) #to print just the first line
print(text.get("2.0", END)) #to print second line to the end
text.pack()




window.mainloop()