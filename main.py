from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash card")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)


import_front_image = PhotoImage(file="./images/card_front.png")
import_back_image = PhotoImage(file="./images/card_back.png")
import_right_image = PhotoImage(file="./images/right.png")
import_wrong_image = PhotoImage(file="./images/wrong.png")


canvas = Canvas()
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=import_back_image)
canvas.create_text(400,100,text="Title", font=("Arial", 30, "normal"))
canvas.create_text(400,300,text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0)


window.mainloop()
