from tkinter import *
import math

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def reset_timer():
    root.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg='#A020F0')
    check_marks.config(text="")
    global reps
    reps = 0

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg='#0000ff')
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg='#00ff00')
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg='#ff0000')

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = root.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)

root = Tk()
root.title("Pomodoro Timer Application")
root.config(padx=100, pady=50, bg="#f7f5dd")

title_label = Label(text="Timer", fg='#A020F0', bg="#f7f5dd", font=("Arial", 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Arial", 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer, bg="#e7305b", font=("arial", 15, "bold"))
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command = reset_timer, bg="#e7305b", font=("arial", 15, "bold"))
reset_button.grid(column=2, row=2)

check_marks = Label(text="", fg='#00FF00', bg="#f7f5dd", font=("arial", 25, "bold"))
check_marks.grid(column=1, row=3)

root.mainloop()
