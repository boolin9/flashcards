from tkinter import *
import csv
import random

BACKGROUND_COLOR = '#B1DDC6'
TEXT_COLOR = '#34444D'

root = Tk()
root.title('tkFlash')
root.config(background=BACKGROUND_COLOR, padx=50, pady=50)

with open('french_words.csv') as file:
    reader = csv.DictReader(file)
    word_dict = {rows['French']:rows['English'] for rows in reader}

dict_copy = word_dict.copy()
total_words = (len(word_dict.keys()))


def get_random_word():
    global french_word
    global english_word
    random_dict_item = random.sample(dict_copy.items(), 1)
    french_word = random_dict_item[0][0]
    english_word = random_dict_item[0][1]


def turn_card():
    global card_state
    global score_text
    global french_text
    global english_text
    global french_word
    global english_word
    global front_card
    card.delete('all')
    
    
    if card_state:
        front_card = card.create_image(400, 263, image=front_image)
        card.create_text(400, 150, text="French", fill=TEXT_COLOR, font=('Helvetica', 40, 'italic'))
        french_text = card.create_text(400, 263, text=f"{french_word}", fill=TEXT_COLOR, font=('Helvetica', 60, 'bold'))
        score_text = card.create_text(400, 430, text=f'{score}/{total_words}', fill=TEXT_COLOR, font=('Helvetica', 20, 'bold'))

    else:
        card.create_image(400, 263, image=back_image)
        card.create_text(400, 150, text="English", fill=TEXT_COLOR, font=('Helvetica', 40, 'italic'))
        english_text = card.create_text(400, 263, text=f"{english_word}", fill=TEXT_COLOR, font=('Helvetica', 60, 'bold'))
        score_text = card.create_text(400, 430, text=f'{score}/{total_words}', fill=TEXT_COLOR, font=('Helvetica', 20, 'bold'))

    card_state = not card_state


def correct_answer():
    global card_state
    global score
    global score_text
    global french_text
    global english_text
    global french_word
    global english_word
    if score < total_words:
        score += 1
        get_random_word()
        card_state = True
        turn_card()
        del dict_copy[french_word]
            

def wrong_answer():
    global card_state
    global score
    global score_text
    global french_text
    global english_text
    global french_word
    global english_word
    global random_dict_item
    if score < total_words:
        get_random_word()
        card_state = True
        turn_card()


card_state = True
score = 0

card = Canvas(root, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card.grid(column=0, row=0, columnspan=3)

front_image = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file='images/card_back.png')
rbutton_image = PhotoImage(file='images/right.png')
wbutton_image = PhotoImage(file='images/wrong.png')
tbutton_image = PhotoImage(file='images/turn.png')

right_button = Button(image=rbutton_image, highlightbackground=BACKGROUND_COLOR, command=correct_answer)
right_button.grid(column=0, row=1)

wrong_button = Button(image=wbutton_image, highlightbackground=BACKGROUND_COLOR, command=wrong_answer)
wrong_button.grid(column=2, row=1)

turn_button = Button(image=tbutton_image, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR, command=turn_card)
turn_button.grid(column=1, row=1)

get_random_word()
turn_card()


root.mainloop()