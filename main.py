from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, highlightthickness=0, bg='white')
add_button.grid(column=1, row=4, columnspan=2)

# Image
lock_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

window.mainloop()