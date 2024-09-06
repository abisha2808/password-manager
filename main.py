from tkinter import *
from tkinter import messagebox
#Password Generator Project
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

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for c in range(randint(2, 4))]
    password_list += [choice(numbers) for n in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")

    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(password) == 0 or len(website) == 0:
        messagebox.showwarning(title="warning", message="Don't leave any thing empty")

    else:
        #input = messagebox.askokcancel(title=website,
        # message=f"The website that entered are \nEmail: {email}\n password:{password}\n Are you want to save this?")
        #if input == "ok":
        try:
            with open("data.json", mode="r") as data_file:
                info = json.load(data_file)
                print(type(info))

        except FileNotFoundError:

            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            info.update(new_data)

            with open("data.json", mode="w") as data_file:
                json.dump(info, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


#-----------------------------search password---------------------------#

def search():
    website = website_entry.get()
    email = email_entry.get()
    if len(website) == 0:
        messagebox.showwarning(title="warning", message="Don't leave any thing empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="No Data file found.")
        else:
            if website in data:
                if data[website]["email"] == email:
                    messagebox.showinfo(title=website, message=f"Email:{email} \nPassword:{data[website]["password"]}")
            else:
                messagebox.showwarning(title="Error", message=f"There is no password saved for the {website} website")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="EW")

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "janeabisha28@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

password_button = Button(text="Generate Password", command=generate_password, highlightthickness=0)
password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=40, command=save_password, highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

search_button = Button(text="Search", highlightthickness=0, command=search)
search_button.grid(column=2, row=1, sticky="EW")

window.mainloop()
