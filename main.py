from tkinter import *
from tkinter import messagebox
import random


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


# ---------------------------- SAVE PASSWORD ------------------------------- #
def store_account():
    pw_content = password_text.get()
    email_content = email_text.get()
    website_content = website_text.get()
    full_account = f"{website_content} | {email_content} | {pw_content}\n"

    if len(pw_content) == 0 or len(website_content) == 0:
        messagebox.showerror(title="Invalid Input", message="Must enter valid values")
        return None

    is_ok = messagebox.askokcancel(title=website_content, message=f"New Account: {website_content},"
                                                                  f" \nUsername: {email_content},"
                                                                  f" \n Password: {pw_content}")
    if is_ok:
        with open("data.txt", 'a') as file:
            file.write(full_account + '\n')
            password_text.delete(0, END)
            website_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg='white')

# Labels
website_label = Label(text="Website Url:", bg='white', fg='black')
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg='white', fg='black')
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg='white', fg='black')
password_label.grid(column=0, row=3)

# Text boxes
website_text = Entry(bg='white', width=35, fg='black')
website_text.grid(column=1, row=1, columnspan=2)
website_text.focus()
email_text = Entry(bg='white', width=35, fg='black')
email_text.insert(0, "dariusid08@gmail.com")
email_text.grid(column=1, row=2, columnspan=2)
password_text = Entry(bg='white', width=21, fg='black')
password_text.grid(column=1, row=3)

# Buttons
generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, highlightthickness=0, bg='white', command=store_account)
add_button.grid(column=1, row=4, columnspan=2)

# Image
lock_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

window.mainloop()
