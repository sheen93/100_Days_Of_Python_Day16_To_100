from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_DATA = {
    "Spanish" : "data/spanish/spanish_words.csv",
    "French" : "data/french/frecnh_words.csv"
}

class WelcomeWindow:
    def __init__(self,root):
        self.root = root # defining self for welcome screen
        self.root.title("Welcome to Flashy Pro")
        self.root.config(padx=50, pady=50, bg= BACKGROUND_COLOR)

        Label(root, text="language: ", bg=BACKGROUND_COLOR, font= ("Ariel", 20)).grid(column=1, row=0)

        Button(root, text="Spanish", command=lambda: self.start_app("Spanish")).grid(column=0, row=1)
        Button(root, text= "French", command=lambda: self.start_app("French")).grid(column=3, row=1)

    def start_app(self, language):
        self.root.destroy() # destroy welcome screen

        main_root = Tk() # main page layer
        app = FlashyApp(main_root, language)
        main_root.mainloop()

class FlashyApp:
    def __init__(self, window, language):
        self.window = window
        self.language = language
        self.file_path = LANGUAGE_DATA[language]
        self.window.title("Flashy Pro")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        # state variables
        self.current_card = {}
        self.flip_timer = None
        self.word_dict = self.load_data()

        # ui elements
        self.canvas = Canvas(window, height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.front_img = PhotoImage(file="images/card_front.png")
        self.back_img = PhotoImage(file="images/card_back.png")
        self.card_background = self.canvas.create_image(400, 263, image=self.front_img)
        self.card_title = self.canvas.create_text(400, 150, text="Title", font=("Ariel", 20, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))
        self.canvas.grid(column=0,row=0, columnspan=3)

        # buttons
        self.known_img = PhotoImage(file="images/right.png")
        self.known_button = Button(image=self.known_img, highlightthickness=0, command=self.remove_item)
        self.known_button.grid(column=0, row=1)

        self.flip_img = PhotoImage(file="images/flip.png")
        self.flip_button = Button(image=self.flip_img, height=100, width=100,  highlightthickness=0, command=self.flip_card, background=BACKGROUND_COLOR)
        self.flip_button.grid(column=1,row=1)

        self.unknown_img = PhotoImage(file="images/wrong.png")
        self.unknown_button = Button(image=self.unknown_img, highlightthickness=0, command=self.next_card)
        self.unknown_button.grid(column=2, row=1)


    def next_card(self):
        pass
    def flip_card(self):
        pass
    def remove_item(self):
        pass
    def load_data(self):
        pass

try:
    df = pandas.read_csv("data/word_to_learn.csv")
    word_dict = df.to_dict(orient="records")
except FileNotFoundError:
    df = pandas.read_csv("data/spanish/spanish_words.csv")
    word_dict = df.to_dict(orient="records")
current_card = {}

if __name__ == "__main__":
    root = Tk()
    app = WelcomeWindow(root)
    root.mainloop()


# def next_card():
#     global current_card, flip_timer
#     window.after_cancel(flip_timer)
#     current_card = random.choice(word_dict)
#     spanish_lang_key = list(current_card.keys())[0]
#     canvas.itemconfig(card_background, image=front_img)
#     canvas.itemconfig(card_title, text= spanish_lang_key, fill="black")
#     canvas.itemconfig(card_word, text= current_card["SPANISH"], fill="black")
#     flip_timer = window.after(3000, flip_card)
#
# def remove_known():
#     print(f"{current_card} is known to user")
#     word_dict.remove(current_card)
#     to_learn_df = pandas.DataFrame(word_dict)
#     to_learn_df.to_csv("data/word_to_learn.csv", index=False)
#     next_card()
#
# def flip_card():
#     global current_card
#     try:
#         canvas.itemconfig(card_background, image=back_img)
#         canvas.itemconfig(card_title, text= "English", fill="white")
#         canvas.itemconfig(card_word, text= current_card["ENGLISH"], fill="white")
#     except KeyError:
#         next_card()