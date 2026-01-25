import random
import string
import tkinter as tk

def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        result_label.config(text="Enter a valid number")
        return

    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = ''.join(random.choice(chars) for _ in range(length))
    result_label.config(text=password)

# Window setup
window = tk.Tk()
window.title("Password Generator")
window.geometry("300x200")

# Length input
tk.Label(window, text="Password Length:").pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Generate button
generate_button = tk.Button(window, text="Generate", command=generate_password)
generate_button.pack(pady=10)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack()

window.mainloop()
