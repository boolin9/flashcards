from tkinter import *

BACKGROUND_COLOR = '#B1DDC6'
TEXT_COLOR = '#34444D'

root = Tk()
root.title('tkFlash')
root.config(background=BACKGROUND_COLOR, padx=50, pady=50)


def turn_card():
    back_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    back_image = PhotoImage(file='images/card_back.png')
    back_card.create_image(400, 263, image=back_image)
    back_card.create_text(400, 263, text="French", fill='white', font=('Helvetica', 60, 'bold'))
    back_card.grid(column=0, row=0, columnspan=3)
    front_card.itemconfig(back_card)



def correct_answer():
    pass


def wrong_answer():
    pass


# canvas 
front_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file='images/card_front.png')
front_card.create_image(400, 263, image=card_image)
front_card.create_text(400, 150, text="French", fill=TEXT_COLOR, font=('Helvetica', 40, 'italic'))
front_card.create_text(400, 263, text="Word", fill=TEXT_COLOR, font=('Helvetica', 60, 'bold'))
front_card.create_text(400, 430, text="Word", fill=BACKGROUND_COLOR, font=('Helvetica', 20, 'bold'))
front_card.grid(column=0, row=0, columnspan=3)

# button label
rbutton_image = PhotoImage(file='images/right.png')
wbutton_image = PhotoImage(file='images/wrong.png')
tbutton_image = PhotoImage(file='images/turn.png')

# button
right_button = Button(image=rbutton_image, highlightbackground=BACKGROUND_COLOR)
right_button.grid(column=0, row=1)

# button
wrong_button = Button(image=wbutton_image, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(column=2, row=1)

# button
turn_button = Button(image=tbutton_image, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR, command=turn_card)
turn_button.grid(column=1, row=1)


root.mainloop()