import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox, ttk
import mysql.connector
from datetime import datetime

# ------------------ MySQL Connection ------------------
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'RAHUL123',  # <-- change to your MySQL password
    'database': 'library_db'
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

# ------------------ GUI Application ------------------
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("900x600")

        # Style
        style = tb.Style("litera")

        # Tabs
        self.tab_control = ttk.Notebook(root)
        self.book_tab = ttk.Frame(self.tab_control)
        self.member_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.book_tab, text="Books")
        self.tab_control.add(self.member_tab, text="Members")
        self.tab_control.pack(expand=1, fill="both")

        # Build Book Tab
        self.build_book_tab()

        # Build Member Tab
        self.build_member_tab()

        # Load data
        self.load_books()
        self.load_members()

    # ------------------ BOOK TAB ------------------
    def build_book_tab(self):
        # Labels and Entries
        tb.Label(self.book_tab, text="Title:").grid(row=0, column=0, padx=10, pady=10)
        self.title_entry = tb.Entry(self.book_tab)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)

        tb.Label(self.book_tab, text="Author:").grid(row=1, column=0, padx=10, pady=10)
        self.author_entry = tb.Entry(self.book_tab)
        self.author_entry.grid(row=1, column=1, padx=10, pady=10)

        tb.Label(self.book_tab, text="Genre:").grid(row=2, column=0, padx=10, pady=10)
        self.genre_entry = tb.Entry(self.book_tab)
        self.genre_entry.grid(row=2, column=1, padx=10, pady=10)

        tb.Label(self.book_tab, text="Quantity:").grid(row=3, column=0, padx=10, pady=10)
        self.quantity_entry = tb.Entry(self.book_tab)
        self.quantity_entry.grid(row=3, column=1, padx=10, pady=10)

        # Buttons
        tb.Button(self.book_tab, text="Add Book", bootstyle=SUCCESS, command=self.add_book).grid(row=4, column=0, padx=10, pady=10)
        tb.Button(self.book_tab, text="Update Book", bootstyle=INFO, command=self.update_book).grid(row=4, column=1, padx=10, pady=10)
        tb.Button(self.book_tab, text="Delete Book", bootstyle=DANGER, command=self.delete_book).grid(row=4, column=2, padx=10, pady=10)

        # Treeview for displaying books
        self.book_tree = ttk.Treeview(self.book_tab, columns=("ID", "Title", "Author", "Genre", "Quantity"), show='headings')
        self.book_tree.heading("ID", text="ID")
        self.book_tree.heading("Title", text="Title")
        self.book_tree.heading("Author", text="Author")
        self.book_tree.heading("Genre", text="Genre")
        self.book_tree.heading("Quantity", text="Quantity")
        self.book_tree.column("ID", width=50)
        self.book_tree.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
        self.book_tree.bind("<<TreeviewSelect>>", self.select_book)

    # ------------------ MEMBER TAB ------------------
    def build_member_tab(self):
        tb.Label(self.member_tab, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        self.member_name_entry = tb.Entry(self.member_tab)
        self.member_name_entry.grid(row=0, column=1, padx=10, pady=10)

        tb.Label(self.member_tab, text="Email:").grid(row=1, column=0, padx=10, pady=10)
        self.member_email_entry = tb.Entry(self.member_tab)
        self.member_email_entry.grid(row=1, column=1, padx=10, pady=10)

        tb.Label(self.member_tab, text="Phone:").grid(row=2, column=0, padx=10, pady=10)
        self.member_phone_entry = tb.Entry(self.member_tab)
        self.member_phone_entry.grid(row=2, column=1, padx=10, pady=10)

        tb.Button(self.member_tab, text="Add Member", bootstyle=SUCCESS, command=self.add_member).grid(row=3, column=0, padx=10, pady=10)
        tb.Button(self.member_tab, text="Update Member", bootstyle=INFO, command=self.update_member).grid(row=3, column=1, padx=10, pady=10)
        tb.Button(self.member_tab, text="Delete Member", bootstyle=DANGER, command=self.delete_member).grid(row=3, column=2, padx=10, pady=10)

        self.member_tree = ttk.Treeview(self.member_tab, columns=("ID", "Name", "Email", "Phone"), show='headings')
        self.member_tree.heading("ID", text="ID")
        self.member_tree.heading("Name", text="Name")
        self.member_tree.heading("Email", text="Email")
        self.member_tree.heading("Phone", text="Phone")
        self.member_tree.column("ID", width=50)
        self.member_tree.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
        self.member_tree.bind("<<TreeviewSelect>>", self.select_member)

    # ------------------ DATABASE OPERATIONS ------------------
    # BOOK FUNCTIONS
    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        quantity = self.quantity_entry.get()

        if title and author and quantity:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO books (title, author, genre, quantity) VALUES (%s, %s, %s, %s)",
                               (title, author, genre, quantity))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Book added successfully!")
                self.clear_book_entries()
                self.load_books()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Title, Author, and Quantity are required.")

    def load_books(self):
        for row in self.book_tree.get_children():
            self.book_tree.delete(row)
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books")
            rows = cursor.fetchall()
            for row in rows:
                self.book_tree.insert("", END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def select_book(self, event):
        selected = self.book_tree.focus()
        if selected:
            values = self.book_tree.item(selected, 'values')
            self.book_id = values[0]
            self.title_entry.delete(0, END)
            self.title_entry.insert(0, values[1])
            self.author_entry.delete(0, END)
            self.author_entry.insert(0, values[2])
            self.genre_entry.delete(0, END)
            self.genre_entry.insert(0, values[3])
            self.quantity_entry.delete(0, END)
            self.quantity_entry.insert(0, values[4])

    def update_book(self):
        try:
            selected = self.book_id
        except AttributeError:
            messagebox.showerror("Error", "Select a book first")
            return

        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        quantity = self.quantity_entry.get()
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE books SET title=%s, author=%s, genre=%s, quantity=%s WHERE book_id=%s",
                           (title, author, genre, quantity, selected))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Book updated successfully!")
            self.clear_book_entries()
            self.load_books()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_book(self):
        try:
            selected = self.book_id
        except AttributeError:
            messagebox.showerror("Error", "Select a book first")
            return
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM books WHERE book_id=%s", (selected,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Book deleted successfully!")
            self.clear_book_entries()
            self.load_books()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_book_entries(self):
        self.title_entry.delete(0, END)
        self.author_entry.delete(0, END)
        self.genre_entry.delete(0, END)
        self.quantity_entry.delete(0, END)

    # MEMBER FUNCTIONS
    def add_member(self):
        name = self.member_name_entry.get()
        email = self.member_email_entry.get()
        phone = self.member_phone_entry.get()
        if name and email:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO members (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Member added successfully!")
                self.clear_member_entries()
                self.load_members()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Name and Email are required.")

    def load_members(self):
        for row in self.member_tree.get_children():
            self.member_tree.delete(row)
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM members")
            rows = cursor.fetchall()
            for row in rows:
                self.member_tree.insert("", END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def select_member(self, event):
        selected = self.member_tree.focus()
        if selected:
            values = self.member_tree.item(selected, 'values')
            self.member_id = values[0]
            self.member_name_entry.delete(0, END)
            self.member_name_entry.insert(0, values[1])
            self.member_email_entry.delete(0, END)
            self.member_email_entry.insert(0, values[2])
            self.member_phone_entry.delete(0, END)
            self.member_phone_entry.insert(0, values[3])

    def update_member(self):
        try:
            selected = self.member_id
        except AttributeError:
            messagebox.showerror("Error", "Select a member first")
            return

        name = self.member_name_entry.get()
        email = self.member_email_entry.get()
        phone = self.member_phone_entry.get()
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE members SET name=%s, email=%s, phone=%s WHERE member_id=%s",
                           (name, email, phone, selected))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Member updated successfully!")
            self.clear_member_entries()
            self.load_members()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_member(self):
        try:
            selected = self.member_id
        except AttributeError:
            messagebox.showerror("Error", "Select a member first")
            return
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM members WHERE member_id=%s", (selected,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Member deleted successfully!")
            self.clear_member_entries()
            self.load_members()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_member_entries(self):
        self.member_name_entry.delete(0, END)
        self.member_email_entry.delete(0, END)
        self.member_phone_entry.delete(0, END)

# ------------------ MAIN ------------------
if __name__ == "__main__":
    root = tb.Window(themename="superhero")
    app = LibraryApp(root)
    root.mainloop()
