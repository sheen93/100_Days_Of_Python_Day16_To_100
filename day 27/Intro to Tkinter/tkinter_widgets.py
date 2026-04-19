from tkinter import *

#window creation
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

#spinbox
def spinbox_used():
    print(spinbox.get()) #gets the current value in spinbox

spinbox = Spinbox(from_=-10, to=10, width=5, command=spinbox_used)
spinbox.pack()

#scale
def scale_used(value):
    print(value) #called with current scale value
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#checkbutton
def checkbutton_used():
    print(checked_state.get()) #Prints 1 if On button checked, otherwise 0
checked_state = IntVar() #variable to hold on to checked state, 0 is off, 1 is on
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#radiobutton
def radio_used():
    print(radio_state.get())
radio_state = IntVar() #Variable to hold on to which radio button is checked
radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection())) #gets current selection from listbox

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()