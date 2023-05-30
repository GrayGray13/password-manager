from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = user_entry.get()
    password = pass_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Missing Data", message="There is missing data for the password\nPlease "
                                                          "try again.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered for {website}:\nUsername: {username}\n"
                                               f"Password: {password}\nWould you like to save?")

        if is_ok:
            data = f"{website} | {username} | {password}\n"
            with open("data.txt", mode="a") as file:
                file.write(data)
            website_entry.delete(0, END)
            user_entry.delete(0, END)
            user_entry.insert(0, "test@gmail.com")
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)

website_label = Label(text="Website:")
user_label = Label(text="Email/Username:")
pass_label = Label(text="Password:")

website_entry = Entry()
user_entry = Entry()
pass_entry = Entry(width=30)

pass_gen_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=30, command=save)

canvas.grid(column=1, row=0)
website_label.grid(column=0, row=1)
website_entry.grid(columnspan=2, column=1, row=1, padx=5, pady=2, sticky="ew")
website_entry.focus()
user_label.grid(column=0, row=2)
user_entry.grid(columnspan=2, column=1, row=2, padx=5, pady=2, sticky="ew")
user_entry.insert(0, "test@gmail.com")
pass_label.grid(column=0, row=3, sticky="ew")
pass_entry.grid(column=1, row=3, padx=5, sticky="w")
pass_gen_button.grid(column=2, row=3, padx=5, pady=2, sticky="ew")
add_button.grid(column=1, columnspan=2, row=4, padx=5, pady=2, sticky="ew")

window.mainloop()
