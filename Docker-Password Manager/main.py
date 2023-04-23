from tkinter import *
from tkinter import messagebox  # special dialogue boxes (pop-ups)
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator
def Generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    # for char in password_list:
    #     password += char
    password="".join(password_list)
    password_ip.insert(0, password)

    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_ip.get()         # get() method is used to retrieve the input in entry method
    email_data = mail_ip.get()
    password_data = password_ip.get()
    flag = True
    if len(website_data) == 0 or len(password_data) == 0 or len(email_data) == 0:     # in case if any field is left empty
        messagebox.showinfo(title="Oops", message="Please dont leave any field empty.")  # show message dialogue box
        flag = False

    if flag:
        is_ok = messagebox.askokcancel(title=website_data,
                                       message=f"Your credentials are:\nEmail: {email_data}\nPassword: {password_data}")
        # ok & cancel pop up box and return true if 'ok' and false if 'cancel' is pressed
        with open("data.text", "a") as data_file:
            data_file.write(f"{website_data} | {email_data} | {password_data}\n")
            website_ip.delete(0, END)
            password_ip.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_ip = Entry(width=35)
website_ip.grid(column=1, row=1, columnspan=2)
website_ip.focus()  # lets the cursor straight to corresponding entry box
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)    # used to relocate the attribute in the from of rows and columns

mail_ip = Entry(width=35)   # entry box
mail_ip.grid(column=1, row=2, columnspan=2)   # columnspan is used if your attribute is covering more than one column
mail_label = Label(text="Email/Username: ")
mail_label.grid(column=0, row=2)
mail_ip.insert(0, "jalajsrivastav21@gmail.com")  # prefilled details (often used)

password_ip = Entry(width=25)
password_ip.grid(column=1, row=3)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

password_button = Button(text="Generate", command=Generate_password)
password_button.grid(column=2, row=3, columnspan=2)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
