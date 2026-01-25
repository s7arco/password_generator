import random
import string
import tkinter as tk

def password_generator():
    length = int(plength_entry.get())
    password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))
    result_label.config(text=password)

# Setup window
window = tk.Tk()
window.title("Password Generator")
window.geometry("500x300")

# Title & PLength input
Title = tk.Label(text="Password Generator",
                 background="White").pack(pady=20)
label = tk.Label(text="Password Length:")
plength_entry = tk.Entry()
label.pack()
plength_entry.pack()

# Create button
button = tk.Button(text="Generate", command=password_generator)
button.pack(pady=20)

result_label = tk.Label(text="")
result_label.pack()


window.mainloop()
