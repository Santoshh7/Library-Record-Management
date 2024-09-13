import tkinter as tk
from tkinter import messagebox
import mysql.connector as c
import datetime

# Connecting to the MySQL database
mydb = c.connect(
    host="localhost",
    user="root",
    password="ALLhappYtogether07*",
    database="library"
)

# Functions

def add_user():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        sql = "INSERT INTO login (username, password) VALUES (%s, %s)"
        data = (username, password)
        cursor = mydb.cursor()
        cursor.execute(sql, data)
        mydb.commit()
        messagebox.showinfo("Success", f"User {username} added successfully!")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in both fields.")

def delete_user():
    username = username_entry.get()
    if username:
        sql = "DELETE FROM login WHERE username = %s"
        data = (username,)
        cursor = mydb.cursor()
        cursor.execute(sql, data)
        mydb.commit()
        messagebox.showinfo("Success", f"User {username} deleted successfully!")
        username_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a username.")

def display_users():
    sql = "SELECT username, password FROM login"
    cursor = mydb.cursor()
    cursor.execute(sql)
    users = cursor.fetchall()
    users_list.delete(0, tk.END)
    for user in users:
        users_list.insert(tk.END, f"Username: {user[0]}, Password: {user[1]}")

def admin_panel():
    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Panel")
    
    tk.Label(admin_window, text="Username:").grid(row=0, column=0)
    tk.Entry(admin_window, textvariable=username_var).grid(row=0, column=1)
    
    tk.Label(admin_window, text="Password:").grid(row=1, column=0)
    tk.Entry(admin_window, textvariable=password_var).grid(row=1, column=1)
    
    tk.Button(admin_window, text="Add User", command=add_user).grid(row=2, column=0, pady=10)
    tk.Button(admin_window, text="Delete User", command=delete_user).grid(row=2, column=1, pady=10)
    tk.Button(admin_window, text="Display Users", command=display_users).grid(row=3, column=0, pady=10)
    
    tk.Label(admin_window, text="Users List:").grid(row=4, column=0, columnspan=2)
    users_list.grid(row=5, column=0, columnspan=2, pady=10)

def library_menu():
    user_window = tk.Toplevel(root)
    user_window.title("Library Management System")

    tk.Button(user_window, text="Add Book", command=add_book).grid(row=0, column=0, pady=10, padx=10)
    tk.Button(user_window, text="Issue Book", command=issue_book).grid(row=1, column=0, pady=10, padx=10)
    tk.Button(user_window, text="Submit Book", command=submit_book).grid(row=2, column=0, pady=10, padx=10)
    tk.Button(user_window, text="Delete Book", command=delete_book).grid(row=3, column=0, pady=10, padx=10)
    tk.Button(user_window, text="Display Books", command=display_books).grid(row=4, column=0, pady=10, padx=10)

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "San" and password == "welcome23":
        messagebox.showinfo("Access Granted", "Welcome, Admin!")
        admin_panel()
    else:
        sql = "SELECT * FROM login WHERE username = %s AND password = %s"
        data = (username, password)
        cursor = mydb.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Success", f"{username} logged in successfully!")
            library_menu()
        else:
            messagebox.showerror("Error", "Username or Password is incorrect!")

def add_book():
    add_book_window = tk.Toplevel(root)
    add_book_window.title("Add Book")

    tk.Label(add_book_window, text="Book Name:").grid(row=0, column=0)
    book_name = tk.Entry(add_book_window)
    book_name.grid(row=0, column=1)

    tk.Label(add_book_window, text="Book Code:").grid(row=1, column=0)
    book_code = tk.Entry(add_book_window)
    book_code.grid(row=1, column=1)

    tk.Label(add_book_window, text="Quantity:").grid(row=2, column=0)
    quantity = tk.Entry(add_book_window)
    quantity.grid(row=2, column=1)

    tk.Label(add_book_window, text="Title/Subject:").grid(row=3, column=0)
    title_subject = tk.Entry(add_book_window)
    title_subject.grid(row=3, column=1)

    def add():
        BOOK_NAME = book_name.get()
        BOOK_CODE = book_code.get()
        QUANTITY = quantity.get()
        TITLE_OR_SUBJECT = title_subject.get()

        if BOOK_NAME and BOOK_CODE and QUANTITY and TITLE_OR_SUBJECT:
            sql = "INSERT INTO book (BOOK_NAME, BOOK_CODE, QUANTITY, TITLE_OR_SUBJECT) VALUES (%s, %s, %s, %s)"
            data = (BOOK_NAME, BOOK_CODE, QUANTITY, TITLE_OR_SUBJECT)
            cursor = mydb.cursor()
            cursor.execute(sql, data)
            mydb.commit()
            messagebox.showinfo("Success", "Book added to the library successfully!")
            add_book_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    tk.Button(add_book_window, text="Add Book", command=add).grid(row=4, column=0, columnspan=2, pady=10)

def issue_book():
    issue_book_window = tk.Toplevel(root)
    issue_book_window.title("Issue Book")

    tk.Label(issue_book_window, text="Name:").grid(row=0, column=0)
    name = tk.Entry(issue_book_window)
    name.grid(row=0, column=1)

    tk.Label(issue_book_window, text="Enrollment Number:").grid(row=1, column=0)
    enrollment_number = tk.Entry(issue_book_window)
    enrollment_number.grid(row=1, column=1)

    tk.Label(issue_book_window, text="Book Code:").grid(row=2, column=0)
    book_code = tk.Entry(issue_book_window)
    book_code.grid(row=2, column=1)

    tk.Label(issue_book_window, text="Date (DD/MM/YYYY):").grid(row=3, column=0)
    date = tk.Entry(issue_book_window)
    date.grid(row=3, column=1)

    def issue():
        NAME = name.get()
        ENROLLMENT_NUMBER = enrollment_number.get()
        BOOK_CODE = book_code.get()
        DATE = date.get()

        # Convert the date from DD/MM/YYYY to YYYY-MM-DD
        try:
            DATE = datetime.datetime.strptime(DATE, '%d/%m/%Y').strftime('%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Date Error", "Incorrect date format. Please enter the date as DD/MM/YYYY.")
            return

        # Check if BOOK_CODE exists in the 'book' table
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM book WHERE BOOK_CODE = %s", (BOOK_CODE,))
        book_exists = cursor.fetchone()

        if not book_exists:
            messagebox.showerror("Error", "Book code does not exist in the library records.")
            return

        if NAME and ENROLLMENT_NUMBER and BOOK_CODE and DATE:
            sql = "INSERT INTO book_issue (NAME, ENROLLMENT_NUMBER, BOOK_CODE, DATE) VALUES (%s, %s, %s, %s)"
            data = (NAME, ENROLLMENT_NUMBER, BOOK_CODE, DATE)
            cursor.execute(sql, data)
            mydb.commit()
            messagebox.showinfo("Success", f"Book issued to {NAME}")
            book_update(BOOK_CODE, -1)
            issue_book_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    tk.Button(issue_book_window, text="Issue Book", command=issue).grid(row=4, column=0, columnspan=2, pady=10)

def submit_book():
    submit_book_window = tk.Toplevel(root)
    submit_book_window.title("Submit Book")

    tk.Label(submit_book_window, text="Name:").grid(row=0, column=0)
    name = tk.Entry(submit_book_window)
    name.grid(row=0, column=1)

    tk.Label(submit_book_window, text="Enrollment Number:").grid(row=1, column=0)
    enrollment_number = tk.Entry(submit_book_window)
    enrollment_number.grid(row=1, column=1)

    tk.Label(submit_book_window, text="Book Code:").grid(row=2, column=0)
    book_code = tk.Entry(submit_book_window)
    book_code.grid(row=2, column=1)

    tk.Label(submit_book_window, text="Date (DD/MM/YYYY):").grid(row=3, column=0)
    date = tk.Entry(submit_book_window)
    date.grid(row=3, column=1)

    def submit():
        NAME = name.get()
        ENROLLMENT_NUMBER = enrollment_number.get()
        BOOK_CODE = book_code.get()
        DATE = date.get()

        cursor = mydb.cursor()


        # Convert the date from DD/MM/YYYY to YYYY-MM-DD
        try:
            DATE = datetime.datetime.strptime(DATE, '%d/%m/%Y').strftime('%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Date Error", "Incorrect date format. Please enter the date as DD/MM/YYYY.")
            return

        # Check if BOOK_CODE exists in the 'book' table
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM book WHERE BOOK_CODE = %s", (BOOK_CODE,))
        book_exists = cursor.fetchone()

        if not book_exists:
            messagebox.showerror("Error", "Book code does not exist in the library records.")
            return

        if NAME and ENROLLMENT_NUMBER and BOOK_CODE and DATE:
            sql = "INSERT INTO book_submit (NAME, BOOK_CODE, ENROLLMENT_NUMBER, DATE) VALUES (%s, %s, %s, %s)"
            data = (NAME, BOOK_CODE, ENROLLMENT_NUMBER, DATE)
            cursor.execute(sql, data)
            mydb.commit()
            messagebox.showinfo("Success", f"Book submitted by {NAME}")
            book_update(BOOK_CODE, 1)
            submit_book_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    tk.Button(submit_book_window, text="Submit", command=submit).grid(row=4, column=0, columnspan=2, pady=10)

def delete_book():
    delete_book_window = tk.Toplevel(root)
    delete_book_window.title("Delete Book")

    tk.Label(delete_book_window, text="Book Code:").grid(row=0, column=0)
    book_code = tk.Entry(delete_book_window)
    book_code.grid(row=0, column=1)

    def delete():
        BOOK_CODE = book_code.get()
        
        cursor = mydb.cursor()
        
        try:
            # First, delete all records from book_issue related to the BOOK_CODE
            sql_issue = "DELETE FROM book_issue WHERE BOOK_CODE = %s"
            cursor.execute(sql_issue, (BOOK_CODE,))
            
            # # Secondly, delete all records from book_submit related to the BOOK_CODE
            sql_submit = "DELETE FROM book_submit WHERE BOOK_CODE = %s"
            cursor.execute(sql_submit, (BOOK_CODE,))

            # Now, delete the book from the book table
            sql_book = "DELETE FROM book WHERE BOOK_CODE = %s"
            cursor.execute(sql_book, (BOOK_CODE,))
            
            mydb.commit()
            messagebox.showinfo("Success", f"Book with code {BOOK_CODE} and all related issues deleted!")
        except c.Error as err:
            mydb.rollback()
            messagebox.showerror("Error", f"Error: {err}")
        finally:
            delete_book_window.destroy()

    tk.Button(delete_book_window, text="Delete", command=delete).grid(row=1, column=0, columnspan=2, pady=10)

def book_update(book_code, quantity_change):
    cursor = mydb.cursor()
    # Update the quantity of the book
    sql = "UPDATE book SET QUANTITY = QUANTITY + %s WHERE BOOK_CODE = %s"
    cursor.execute(sql, (quantity_change, book_code))
    mydb.commit()


def display_books():
    display_books_window = tk.Toplevel(root)
    display_books_window.title("Display Books")

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM book")
    books = cursor.fetchall()
    
    for index, book in enumerate(books):
        tk.Label(display_books_window, text=f"Book Code: {book[1]}").grid(row=index, column=0, sticky=tk.W)
        tk.Label(display_books_window, text=f"Book Name: {book[0]}").grid(row=index, column=1, sticky=tk.W)
        tk.Label(display_books_window, text=f"Quantity: {book[2]}").grid(row=index, column=2, sticky=tk.W)
        tk.Label(display_books_window, text=f"Title/Subject: {book[3]}").grid(row=index, column=3, sticky=tk.W)

# Main Interface
root = tk.Tk()
root.title("Library Records Management System")

username_var = tk.StringVar()
password_var = tk.StringVar()

tk.Label(root, text="Username:").grid(row=0, column=0)
username_entry = tk.Entry(root, textvariable=username_var)
username_entry.grid(row=0, column=1)

tk.Label(root, text="Password:").grid(row=1, column=0)
password_entry = tk.Entry(root, textvariable=password_var, show='*')
password_entry.grid(row=1, column=1)

tk.Button(root, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=10)

users_list = tk.Listbox(root, width=50)

root.mainloop()
