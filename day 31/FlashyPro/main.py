from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pandas.read_csv("data/word_to_learn.csv")
    word_dict = df.to_dict(orient="records")
except FileNotFoundError:
    df = pandas.read_csv("data/EsToEn.csv")
    word_dict = df.to_dict(orient="records")
current_card = {}
flip_timer = None

def random_card():
    global current_card, flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    current_card = random.choice(word_dict)
    spanish_lang_key = list(current_card.keys())[0]
    canvas.itemconfig(card_background, image=front_img)
    canvas.itemconfig(card_title, text= spanish_lang_key, fill="black")
    canvas.itemconfig(card_word, text= current_card["SPANISH"], fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    global current_card
    eng_lang_key = list(current_card.keys())[1]
    canvas.itemconfig(card_background, image=back_img)
    canvas.itemconfig(card_title, text= eng_lang_key, fill="white")
    canvas.itemconfig(card_word, text= current_card["ENGLISH"], fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas_height = 526
canvas_width = 800
canvas_center_x = canvas_width/2
canvas_center_y = canvas_height/2
canvas = Canvas(window, height=canvas_height, width=canvas_width)

front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(canvas_center_x, canvas_center_y, image=front_img)

card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 20, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))

canvas.grid(column=0,row=0, columnspan=2, sticky="EW")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

known_img = PhotoImage(file="images/right.png")
known_button = Button(image=known_img, highlightthickness=0, command=random_card)
known_button.grid(column=0, row=1)

unknown_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_img, highlightthickness=0, command=random_card)
unknown_button.grid(column=1, row=1)

random_card()


window.mainloop()