from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20, bg="white")

# Labels
website_label = Label(text="Website Url:")

email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# Text boxes
website_text = Entry()
website_text.grid(column=0, row=1)
email_text = Entry()
email_text.grid(column=0 , row=2)
password_text = Entry()
password_text.grid(column=0 , row=3)


lock_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

window.mainloop()