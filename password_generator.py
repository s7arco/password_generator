import random
import string
import tkinter as tk

def password_generator():
    try:
         length = int(plength_entry.get())
    except ValueError:
         result_label.config(text="Enter a valid number")
         return
    
    if length > 18:
         result_label.config(text="Error Max Length: ")
         return
    
    if length < 5:
         result_label.config(text="Error Minimum Length: 6")
         return

    password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))
    result_label.config(text=password)

def copy_password():
     password = result_label.cget("text")
     window.clipboard_clear
     window.clipboard_append(password)

# Setup window
window = tk.Tk()
window.title("Password Generator")
window.geometry("500x300")

# Title & PLength input
Title = tk.Label(text="Password Generator",
                 background="White").pack(pady=20)
label = tk.Label(text="Password Length: ")
plength_entry = tk.Entry()
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
