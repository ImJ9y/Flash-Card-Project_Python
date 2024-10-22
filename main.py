from tkinter import *
import pandas
import random

count = 3

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_frame = original_data.to_dict(orient="records")
else:
    data_frame = data.to_dict(orient="records")

# res = []
current_card = {}

def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_frame)
    # res.append(current_card)
    canvas.itemconfig(front, image=front_image)
    canvas.itemconfig(front_language_label, text="French", fill="black")
    canvas.itemconfig(front_work_label, text=f"{current_card["French"]}", fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(front, image = back_image)
    canvas.itemconfig(front_language_label,text = "English", fill="white")
    canvas.itemconfig(front_work_label, text=f"{current_card["English"]}", fill="white")
    # canvas.itemconfig(front_work_label, text=f"{res[0]["English"]}", fill="white")
    # res.pop()
def learned_word():
    data_frame.remove(current_card)
    data = pandas.DataFrame(data_frame)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_word()


window = Tk()
window.title("Capstone Project")
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg = BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

front = canvas.create_image(400, 263, image = front_image)
canvas.grid(column = 0, row = 0, columnspan = 2) #grid and pack can't use together

#Front Language and Word Labels
front_language_label = canvas.create_text(400, 150, text = "Title", fill="black", font=("Ariel", 40, "italic"))
front_work_label = canvas.create_text(400, 263, text = "Word", fill="black", font=("Ariel", 60, "bold"))

#Correct | Wrong buttons
correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

correct_button = Button(image=correct_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=learned_word)
correct_button.grid(column = 1, row = 1)
wrong_button = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=generate_word)
wrong_button.grid(column = 0, row = 1)


generate_word()

window.mainloop()



