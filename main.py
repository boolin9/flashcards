from tkinter import *

BACKGROUND_COLOR = '#B1DDC6'
TEXT_COLOR = '#34444D'

root = Tk()
root.title('tkFlash')
root.config(background=BACKGROUND_COLOR, padx=50, pady=50)


def turn_card():
    global card_state
    card.delete('all')
    
    if card_state:
        card.create_image(400, 263, image=front_image)
        card.create_text(400, 150, text="French", fill=TEXT_COLOR, font=('Helvetica', 40, 'italic'))
        card.create_text(400, 263, text="Word", fill=TEXT_COLOR, font=('Helvetica', 60, 'bold'))
        card.create_text(400, 430, text="Word", fill=BACKGROUND_COLOR, font=('Helvetica', 20, 'bold'))
    else:
        card.create_image(400, 263, image=back_image)
        card.create_text(400, 263, text="French", fill='white', font=('Helvetica', 60, 'bold'))

    card_state = not card_state


def correct_answer():
    pass


def wrong_answer():
    pass


card_state = True 

card = Canvas(root, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card.grid(column=0, row=0, columnspan=3)

front_image = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file='images/card_back.png')
rbutton_image = PhotoImage(file='images/right.png')
wbutton_image = PhotoImage(file='images/wrong.png')
tbutton_image = PhotoImage(file='images/turn.png')

right_button = Button(image=rbutton_image, highlightbackground=BACKGROUND_COLOR)
right_button.grid(column=0, row=1)

wrong_button = Button(image=wbutton_image, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(column=2, row=1)

turn_button = Button(image=tbutton_image, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR, command=turn_card)
turn_button.grid(column=1, row=1)

turn_card()


root.mainloop()