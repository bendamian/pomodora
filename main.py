from tkinter import *
from tkinter import ttk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# create a window
window = Tk()
window.title('Pomodoro')
# window.geometry('220x224')
window.config(padx=100, pady=50, bg=YELLOW)

# widgets
label1 = ttk.Label(window, text='Label 1', background='red')
label2 = ttk.Label(window, text='Label 2', background='blue')
button1 = ttk.Button(window, text='start')
button2 = ttk.Button(window, text='rest')

canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(110, 112, image=tomato_img)
canvas.create_text(103, 130, text="00.00", fill="white", font=(FONT_NAME, 35, 'bold'))

# define a grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
window.columnconfigure(2, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=3)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)

label1.grid(row=0, column=1, sticky='n')
canvas.grid(row=1, column=1, sticky='nsew')
button1.grid(row=3, column=0, sticky='w')
button2.grid(row=3, column=2, sticky='e')
label2.grid(row=4, column=1, sticky='')

# run
window.mainloop()
