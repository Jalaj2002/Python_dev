from tkinter import *

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
    window.after_cancel(timer)
    canvas.itemconfigure(timer_text,text="00:00")
    label.configure(text="Timer")
    checkmark.configure(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60

    if reps % 8 == 0:
        countDown(long_break)
        label.configure(text="Break", fg=RED)
    if reps % 2 == 0:
        countDown(short_break)
        label.configure(text="Break", fg=PINK)
    else:
        countDown(work_sec)
        label.configure(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(count):
    min_rem = count // 60
    sec_rem = count % 60
    if sec_rem < 10:  # ...1
        sec_rem = '0' + str(sec_rem)  # ........ Dynamic Typing
    canvas.itemconfig(timer_text, text=f"{min_rem}:{sec_rem}")
    if count > 0:
        global timer
        timer = window.after(1000, countDown, count - 1)
    else:
        start_timer()
        mark = ''
        for _ in range(reps // 2):
            mark += '✔️'
        checkmark.configure(text=mark, fg=GREEN, bg=YELLOW)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Tomato Timer")
label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40))
label.grid(column=1, row=0)

window.configure(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=tomato_image)  # takes input in format of photograph
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))  # adds text on image

# countDown(5)
# window.after(1000, countDown, count)
canvas.grid(column=1, row=1)

start_button = Button(text="Start", fg="Black", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", fg="Black", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)
window.mainloop()
