import tkinter as tk
from tkinter import messagebox

# 1. Create the main window
root = tk.Tk()
root.title("My First Python App")
root.geometry("300x150")

# 2. Define a function for the button click
def show_message():
    messagebox.showinfo("Success", "Hello World! You built a desktop app!")

# 3. Add a button widget
button = tk.Button(root, text="Click Me", command=show_message)
button.pack(expand=True)

# 4. Start the application loop
root.mainloop()
