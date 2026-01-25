import random
import string
import tkinter as tk

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
button = tk.Button(text="Generate")
button.pack(pady=20)


window.mainloop()
"""
def password_generator(length):
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))

print("Password Generator")
user_length = int(input("Password Length: "))

password = password_generator(user_length)
print(password)
"""
