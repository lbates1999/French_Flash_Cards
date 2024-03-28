from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
import csv
import random

BACKGROUND_COLOR = "#B1DDC6"
french_words = []
english_words= []
need_to_study = []

current_word = random.randint(1, 101)

with open("data/french_words.csv", "r") as french_word:
    csv_reader = csv.reader(french_word)
    for row in csv_reader:
        french_words.append(row[0])
        english_words.append(row[1].rstrip('\n'))
window = Tk()
window.title("French Flash Cards")
img2 = ImageTk.PhotoImage(Image.open("images/card_back.png"))
current_state = "French"
def turn_card():
    global img2, current_state
    if current_state == "French":
        front_card.configure(text=english_words[current_word], image=img2, compound="center")
        current_state = "English"
    else:
        front_card.configure(text=french_words[current_word], image=img, compound="center")
        current_state = "French"


def got_it_right():
    global current_word, current_state
    current_word = random.randint(1, 102)
    front_card.configure(text=french_words[current_word], image=img, compound="center")
    current_state = "French"
def got_it_wrong():
    global current_word, current_state, need_to_study
    study_word = [f"{french_words[current_word]}, {english_words[current_word]}"]
    if study_word not in need_to_study:
        with open("need_to_study.csv", "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([study_word])
    current_word = random.randint(1, 102)
    front_card.configure(text=french_words[current_word], image=img, compound="center")
    current_state = "French"





img = ImageTk.PhotoImage(Image.open("images/card_front.png"))
front_card = Button(window, text=french_words[current_word], font=("Arial", 30),  image=img, bg=BACKGROUND_COLOR, compound="center", command=turn_card)
front_card.grid(column=0, row=0, columnspan=2)

window.configure(bg=BACKGROUND_COLOR)
img3 = ImageTk.PhotoImage(Image.open("images/right.png"))
panel2 = Button(window,  image=img3, bg=BACKGROUND_COLOR, command=got_it_right)
panel2.grid(column=1, row=1, columnspan=1)
img4 = ImageTk.PhotoImage(Image.open("images/wrong.png"))
panel2 = Button(window,  image=img4, bg=BACKGROUND_COLOR, command=got_it_wrong)
panel2.grid(column=0, row=1, columnspan=1)



window.mainloop()