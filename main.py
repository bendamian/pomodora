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
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label1_string.set("Timer")
    label2_string.set("")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_brea_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_brea_sec)
        label1_string.set(value="Long Break")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label1_string.set(value="Short Break")
    else:
        count_down(work_sec)
        label1_string.set(value="Working")
        label1.config(foreground=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        label2_string.set(mark)


# ---------------------------- UI SETUP ------------------------------- #
# create a window
window = Tk()
window.title('Pomodoro')
# window.geometry('220x224')
window.config(padx=100, pady=50, bg=YELLOW)

# widgets
label1_string = StringVar(value="timer")
label2_string = StringVar(value="")
label1 = Label(window, text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50), textvariable=label1_string)
label2 = Label(window, text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25), textvariable=label2_string)
button1 = Button(window, text='Start', command=start_timer)
button2 = Button(window, text='Reset', command=reset_timer)

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
