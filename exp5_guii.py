import sqlite3
from tkinter import *
from tkinter import ttk

# Database Initialization
conn = sqlite3.connect('registration.db')
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, gender TEXT, contact TEXT, city TEXT, hobbies TEXT)''')
conn.commit()

def create_record():
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
    
    # Display data
    display_data()

def read_records():
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    display_text = ""
    for row in rows:
        display_text += f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}, Contact: {row[4]}, City: {row[5]}, Hobbies: {row[6]}\n"
    d1.delete('1.0', 'end')
    d1.insert('end', display_text)

def update_record():
    # Your code for updating a record goes here
    pass

def delete_record():
    # Your code for deleting a record goes here
    pass

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

b1 = Button(text="Create", command=create_record)
b1.place(x=180, y=210)

b2 = Button(text="Read", command=read_records)
b2.place(x=250, y=210)

b3 = Button(text="Update", command=update_record)
b3.place(x=320, y=210)

b4 = Button(text="Delete", command=delete_record)
b4.place(x=390, y=210)

d1 = Text()
d1.place(x=50, y=260, width=300, height=300)

root.mainloop()

# Close database connection when exiting
conn.close()
