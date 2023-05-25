from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
word = {}

# read csv file here and oriented there data.
data = pandas.read_csv("data/english_words-Sheet_02.csv")
create_dict = data.to_dict(orient="records")


# create a function kye.
def function_key():
    global word
    word = random.choice(create_dict)
    new_data = word["English"]
    canvas.itemconfig(canvas_text, text="English")
    canvas.itemconfig(canvas_word, text=new_data)


def seen_key():
    bangla_word_data = word["Bangla"]
    canvas.itemconfig(bangla_word, text=bangla_word_data)


window = Tk()
window.title("Flash card")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)


import_front_image = PhotoImage(file="./images/card_front.png")
import_back_image = PhotoImage(file="./images/card_back.png")
import_right_image = PhotoImage(file="./images/right.png")
import_wrong_image = PhotoImage(file="./images/wrong.png")

# Create a canvas for image.
canvas = Canvas()
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=import_back_image)
canvas_text = canvas.create_text(400, 100, text="", font=("Arial", 30, "normal"))
canvas_word = canvas.create_text(400, 270, text="", font=("Arial", 60, "bold"))
bangla_word = canvas.create_text(400, 410, text="Word", font=("Arial", 40, "bold"), fill="Green")
canvas.grid(row=0, column=0, columnspan=2)

# Create a Button.
yes_button = Button()
yes_button.config(image=import_right_image, highlightthickness=1, bg="red", command=function_key)
yes_button.grid(row=1, column=0)

no_button = Button()
no_button.config(image=import_wrong_image, highlightthickness=1, bg="red", command=function_key)
no_button.grid(row=1, column=1)

see_button = Button()
see_button.config(text="Seen", highlightthickness=1, fg="Green", font=("Arial", 10, "bold"), command=seen_key)
see_button.place(x=0, y=430)


function_key()


window.mainloop()
