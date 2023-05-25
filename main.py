from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# read csv file here and oriented there data.
try:
    data = pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/english_words-Sheet_02.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# create a function kye.
def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    new_data = current_card["English"]
    canvas.itemconfig(canvas_text, text="English")
    canvas.itemconfig(canvas_word, text=new_data)
    canvas.itemconfig(bangla_word, text="****")
    canvas.itemconfig(crate_img, image=import_front_image)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv", index=False)

    print(len(to_learn))
    next_card()


def seen_key():
    bangla_word_data = current_card["Bangla"]
    canvas.itemconfig(bangla_word, text=bangla_word_data)


def flip_card():
    new_data = current_card["Bangla"]
    canvas.itemconfig(canvas_text, text="Bangla")
    canvas.itemconfig(canvas_word, text=new_data)
    canvas.itemconfig(crate_img, image=import_back_image)


window = Tk()
window.title("Flash card")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

import_front_image = PhotoImage(file="./images/card_front.png")
import_back_image = PhotoImage(file="./images/card_back.png")
import_right_image = PhotoImage(file="./images/right.png")
import_wrong_image = PhotoImage(file="./images/wrong.png")

# Create a canvas for image.
canvas = Canvas()
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
crate_img = canvas.create_image(400, 263, image=import_front_image)

canvas_text = canvas.create_text(400, 100, text="", font=("Arial", 30, "normal"))
canvas_word = canvas.create_text(400, 270, text="", font=("Arial", 60, "bold"))

bangla_word = canvas.create_text(400, 420, text="Word", font=("Arial", 20, "bold"), fill="Green")

canvas.grid(row=0, column=0, columnspan=2)

# Create a Button.
yes_button = Button()
yes_button.config(image=import_right_image, highlightthickness=1, bg="red", command=is_known)
yes_button.grid(row=1, column=0)

no_button = Button()
no_button.config(image=import_wrong_image, highlightthickness=1, bg="red", command=next_card)
no_button.grid(row=1, column=1)

see_button = Button()
see_button.config(text="Seen", highlightthickness=1, fg="Green", font=("Arial", 10, "bold"), command=seen_key)
see_button.place(x=0, y=430)


next_card()


window.mainloop()
