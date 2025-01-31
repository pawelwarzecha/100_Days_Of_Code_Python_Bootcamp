from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_input.delete(0, 'end')

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = letters[:nr_letters] + numbers[:nr_numbers] + symbols[:nr_symbols]
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_line = f"{website} | {email} | {password}"

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Empty fields found!")
    else:
        confirmation = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                                     f" \nPassword: {password} \nIs it okay to save?")
        if confirmation:
            with open("data.txt", "a") as data:
                data.write(new_line + "\n")
                website_input.delete(0, 'end')
                email_input.delete(0, 'end')
                password_input.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo =PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Inputs
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="EW")
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_input.insert(0, "email@email.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="EW")

#Buttons
add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(row=3, column=2, sticky="EW")

window.mainloop()