from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Missing Data", message="There is missing data for the password\nPlease "
                                                          "try again.")
    else:
        data = f"{website} | {username} | {password}\n"
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            user_entry.delete(0, END)
            user_entry.insert(0, "test@gmail.com")
            pass_entry.delete(0, END)


# --------------------------- Find Password ------------------------------- #
def find_password():
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        website = website_entry.get()
        if data.get(website) is None:
            messagebox.showinfo(title="Error", message="No details for the website exists")
        else:
            username = data.get(website)["username"]
            password = data.get(website)["password"]
            messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")


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

website_entry = Entry(width=30)
user_entry = Entry()
pass_entry = Entry(width=30)

search_button = Button(text="Search", command=find_password)
pass_gen_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=30, command=save)

canvas.grid(column=1, row=0)
website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1, padx=5, sticky="ew")
website_entry.focus()
search_button.grid(column=2, row=1, padx=5, pady=2, sticky="ew")
user_label.grid(column=0, row=2)
user_entry.grid(columnspan=2, column=1, row=2, padx=5, pady=2, sticky="ew")
user_entry.insert(0, "test@gmail.com")
pass_label.grid(column=0, row=3, sticky="ew")
pass_entry.grid(column=1, row=3, padx=5, sticky="ew")
pass_gen_button.grid(column=2, row=3, padx=5, pady=2, sticky="ew")
add_button.grid(column=1, columnspan=2, row=4, padx=5, pady=2, sticky="ew")

window.mainloop()
