from tkinter import *
import math
import ttkbootstrap as ttk

# from tkinter import ttk

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
def start_timer():
    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
# create a window
window = Tk()
window.title('Pomodoro')
# window.geometry('220x224')
window.config(padx=100, pady=50, bg=YELLOW)

# widgets
label1 = Label(window, text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
label2 = Label(window, text='✔', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25))
button1 = Button(window, text='Start', command=start_timer)
button2 = Button(window, text='Reset')

canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(110, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00.00", fill="white", font=(FONT_NAME, 35, 'bold'))

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
label2.grid(row=4, column=1, )

# run
window.mainloop()
