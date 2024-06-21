import tkinter as tk
from tkinter import messagebox

def show_dialog():
    messagebox.showinfo("Custom Dialog", "This is a custom dialog box!")

def submit():
    name = name_entry.get()
    gender = gender_var.get()
    hobby = hobby_var.get()
    
    messagebox.showinfo("Submission", f"Name: {name}\nGender: {gender}\nHobby: {hobby}")

# Create main window
root = tk.Tk()
root.title("GUI Example")

# Set the size of the main window
root.geometry("400x250")

# Labels
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w")
tk.Label(root, text="Gender:").grid(row=1, column=0, sticky="w")
tk.Label(root, text="Hobby:").grid(row=2, column=0, sticky="w")

# Textbox
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Radio Buttons
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=1, column=1, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=1, column=1, sticky="e")

# Checkboxes
hobby_var = tk.StringVar()
hobby_var.set("Reading")
tk.Checkbutton(root, text="Reading", variable=hobby_var, onvalue="Reading", offvalue="").grid(row=2, column=1, sticky="w")
tk.Checkbutton(root, text="Gaming", variable=hobby_var, onvalue="Gaming", offvalue="").grid(row=2, column=1, sticky="e")

# Submit Button
tk.Button(root, text="Submit", command=submit).grid(row=3, column=0, columnspan=2, pady=10)

# Custom Dialog Button
tk.Button(root, text="Show Custom Dialog", command=show_dialog).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
