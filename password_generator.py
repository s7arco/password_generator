import random
import string
import tkinter as tk

def password_generator():
    username = username_entry.get()

    if username.strip() == "":
          result_label.config(text="Error: Enter a username!")
          return False
    try:
         length = int(plength_entry.get())
    except ValueError:
         result_label.config(text="Error: Enter a valid Password Length!")
         return False
    
    if length > 18:
         result_label.config(text="Error Max Length: ")
         return False
    
    if length < 5:
         result_label.config(text="Error Minimum Length: 5")
         return False

    password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))
    result_label.config(text=password)
    return True

def copy_password():
     if password_generator() == False:
          result_label.config(text="Enter a valid username and password length!")
          return False

     password = result_label.cget("text")
     window.clipboard_clear()
     window.clipboard_append(password)
     return True

# Setup window
window = tk.Tk()
window.title("Password Generator")
window.geometry("500x300")

# Title & PLength input
Title = tk.Label(text="Password Generator",
                 background="White").pack(pady=20)
username_label = tk.Label(text="Username: ")
username_entry = tk.Entry()
label = tk.Label(text="Password Length: ")
plength_entry = tk.Entry()
username_label.pack()
username_entry.pack()
label.pack()
plength_entry.pack()


# Create button to generate password
button = tk.Button(text="Generate", command=password_generator)
button.pack(pady=20)

# Button to copy onto clipboard for pasting
copy_button = tk.Button(text="Copy", command=copy_password)


result_label = tk.Label(text="")
result_label.pack(pady=10)
copy_button.pack(pady=20)


window.mainloop()
