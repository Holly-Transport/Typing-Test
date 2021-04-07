from tkinter import *
from words import WordBank

BACKGROUND_COLOR = "#B1DDC6"
TIMER_COLOR = "#a3d2ca"
BUTTON_COLOR = "#ffd3b4"
count = 60
score = 0

#--------------Words-----------------#

words = WordBank()
list = words.WordList()

#--------------Timer-----------------#

def timer ():
    global count
    global score
    score = 0
    count -=1
    canvas.itemconfig(timer_text, text=f"{count}")
    if count == 0:
        check()
        count = 60
    else:
        canvas.after(1000, timer)

#--------------Word Check and Score -----------------#

def check ():
    global score
    to_check = text.get("1.0",END)
    to_check = to_check.split(" ")
    flat_list = [item for sublist in list for item in sublist]
    for word in to_check:
        if word in flat_list:
            score +=1
    label_score.config(text= f"Your score is {score} words per minute.")

#--------------UI-----------------#

# Set up Window
window = Tk()
window.title ("Typing Test")
window.minsize(width = 850, height = 590)
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)


# Set up Canvas for Typing Test Words and Timer
canvas = Canvas(width=800, height = 526, highlightthickness=0, bg =BACKGROUND_COLOR)
front = PhotoImage(file="./images/card_front.png")
card = canvas.create_image(400,265, image =front)
timer_text = canvas.create_text(400,30, text="00:00", fill = TIMER_COLOR, font = ("Didot", 35, "bold"))
words = canvas.create_text(400,263, text=list, font = ("Didot", 25), width = 575)
canvas.grid(column=1, row=3, columnspan=2)

# Labels
label_title = Label(text = "Typing Test", font = ("Didot", 56), foreground = "white", background = BACKGROUND_COLOR, pady=5)
label_title.grid(column=1, row = 1, columnspan=2)

label_directions = Label(text = "Try to type as many of the following randomly generated \nwords within one minute to receive your score\n (correct words per minute).", font = ("Didot", 24), foreground = "black", background = BACKGROUND_COLOR, pady=30)
label_directions.grid(column=1, row = 2, columnspan=2)

label_score = Label(text= f"Your score is {score} words per minute.", font = ("Didot", 24), foreground = "black", background = BACKGROUND_COLOR, pady=10)
label_score.grid(column=3, row = 4, columnspan=2)

# Button
# start = PhotoImage (file="./images/start.png")
start_button = Button(text = "Start!", font = ('didot', 24), relief = "raised", highlightthickness = 0, activebackground = BUTTON_COLOR, command = timer)
start_button.grid(column=1, row = 4, columnspan =2)

# Typing Text Field
text = Text(height=20, width= 50)
text.focus()
text.grid(column=3, row=3)


# Gameplay
window.mainloop()
