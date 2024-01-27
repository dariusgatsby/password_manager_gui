from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_text.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for n in range(nr_letters)]
    symbols_list = [random.choice(symbols) for n in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for n in range(nr_numbers)]
    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)

    password = "".join(password_list)

    password_text.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_to_json(data):
    with open("data.json", 'w') as file:
        json.dump(data, file, indent=4)
        password_text.delete(0, END)
        website_text.delete(0, END)


def store_account():
    pw = password_text.get()
    email = email_text.get()
    website = website_text.get()

    if len(pw) == 0 or len(website) == 0:
        messagebox.showerror(title="Invalid Input", message="Must enter valid values")
        return None

    try:
        new_data = {website: {
            'email': email,
            'password': pw
        }}

        with open("data.json", 'r') as file:
            data = json.load(file)
            data.update(new_data)
    except FileNotFoundError:
        write_to_json(new_data)
    else:
        write_to_json(data)


# ---------------------------- Search Credentials --------------------- #
def search_accounts():
    website = website_text.get()
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
            print(data[website])
    except FileNotFoundError:
        messagebox.showerror(title="No save file", message="No data to be searched")
    except KeyError as error_message:
        messagebox.showerror(title="Non-existent key", message=f"The website {error_message} does not exist here.")
    else:
        messagebox.showinfo(title="As per request", message=f"Username: {data[website]['email']},"
                                                            f" Password: {data[website]['password']}")


# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg='white')

# Labels
website_label = Label(text="Website Url:", bg='white', fg='black')
website_label.grid(column=0, row=1)
email_label = Label(text="Username:", bg='white', fg='black')
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg='white', fg='black')
password_label.grid(column=0, row=3)

# Text boxes
website_text = Entry(bg='white', width=21, fg='black')
website_text.grid(column=1, row=1)
website_text.focus()
email_text = Entry(bg='white', width=38, fg='black')
email_text.insert(0, "dariusid08@gmail.com")
email_text.grid(column=1, row=2, columnspan=2)
password_text = Entry(bg='white', width=21, fg='black')
password_text.grid(column=1, row=3)

# Buttons
generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, highlightthickness=0, bg='white', command=store_account)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text='Search', command=search_accounts, width=13)
search_button.grid(column=2, row=1)

# Image
lock_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

window.mainloop()
