import sqlite3
from tkinter import *
from tkinter import ttk

# Database Initialization
conn = sqlite3.connect('registration.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, gender TEXT, contact TEXT, city TEXT, hobbies TEXT)''')
conn.commit()

def submit_data():
    name = e1.get()
    age = e2.get()
    gender = "Female" if r1.get() == 1 else "Male"
    contact = e4.get()
    city = combo1.get()
    hobbies = combo2.get()
    
    # Insert into database
    c.execute("INSERT INTO users (name, age, gender, contact, city, hobbies) VALUES (?, ?, ?, ?, ?, ?)",
              (name, age, gender, contact, city, hobbies))
    conn.commit()
    
    # Clearing Entry Fields
    clear_entries()
    display_data()

def clear_entries():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e4.delete(0, 'end')
    combo1.set('')
    combo2.set('')

def display_data():
    d1.delete(0, 'end')  # Clear existing data
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    for row in rows:
        d1.insert('end', f"{row[0]}: {row[1]}")  # Display only ID and Name

def delete_data():
    selected_item = d1.get(d1.curselection())  # Get selected item directly
    if selected_item:
        selected_id = selected_item.split(':')[0].strip()  # Extract ID and remove any leading/trailing whitespace
        c.execute("DELETE FROM users WHERE id=?", (selected_id,))
        conn.commit()
        display_data()

def update_data():
    selected_item = d1.get(d1.curselection())  # Get selected item directly
    if selected_item:
        selected_id = selected_item.split(':')[0].strip()  # Extract ID and remove any leading/trailing whitespace
        name = e1.get()
        age = e2.get()
        gender = "Female" if r1.get() == 1 else "Male"
        contact = e4.get()
        city = combo1.get()
        hobbies = combo2.get()
        c.execute("UPDATE users SET name=?, age=?, gender=?, contact=?, city=?, hobbies=? WHERE id=?",
                  (name, age, gender, contact, city, hobbies, selected_id))
        conn.commit()
        clear_entries()
        display_data()

root = Tk()
f = Frame(root, width=400, height=600)
f.pack()

root.title("Registration Page")

l1 = Label(text="Name:")
l1.place(x=95, y=20)

e1 = Entry()
e1.place(x=165, y=20)

l2 = Label(text="Age:")
l2.place(x=95, y=50)

e2 = Entry()
e2.place(x=165, y=50)

l3 = Label(text="Gender:")
l3.place(x=95, y=80)

r1 = IntVar()
r2 = IntVar()
Radiobutton(root, text='Female', value=1, variable=r1).place(x=155, y=80)
Radiobutton(root, text='Male', value=2, variable=r1).place(x=235, y=80)

l4 = Label(text="Contact:")
l4.place(x=95, y=110)

e4 = Entry()
e4.place(x=165, y=110)

l5 = Label(text="City:")
l5.place(x=95, y=140)

combo1 = ttk.Combobox(
    state="readonly",
    values=["Mumbai", "Pune", "Kolkata", "Other"]
)
combo1.place(x=165, y=140)

l6 = Label(text="Hobbies:")
l6.place(x=95, y=170)

combo2 = ttk.Combobox(
    state="readonly",
    values=["Cricket", "Football", "BasketBall", "Other"]
)
combo2.place(x=165, y=170)

b1 = Button(text="Submit", command=submit_data)
b1.place(x=180, y=210)

b2 = Button(text="Delete", command=delete_data)
b2.place(x=250, y=210)

b3 = Button(text="Update", command=update_data)
b3.place(x=320, y=210)

d1 = Listbox()
d1.place(x=50, y=260, width=300, height=300)

# Display existing data
display_data()

root.mainloop()

# Close database connection when exiting
conn.close()
