# 📚 Library Management System

<p align="center">

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/TTKBootstrap-Modern_GUI-7952B3?style=for-the-badge">
<img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white">
<img src="https://img.shields.io/badge/Desktop-Application-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge">

</p>

---

# 📖 Overview

The **Library Management System** is a desktop application developed using **Python**, **TTKBootstrap**, **Tkinter**, and **MySQL** to simplify the management of books and library members.

The system provides a modern graphical interface for maintaining book inventories and member records through complete CRUD (Create, Read, Update, Delete) operations. It is designed for schools, colleges, universities, and small libraries that require an efficient and user-friendly management solution.

---

# ✨ Features

## 📚 Book Management

- Add New Books
- Update Book Information
- Delete Books
- View All Books
- Manage Book Inventory
- Store Author Details
- Store Genre Information
- Quantity Management

---

## 👨‍🎓 Member Management

- Register New Members
- Update Member Information
- Delete Members
- View All Members
- Store Email Address
- Store Phone Number

---

## 🖥️ Modern User Interface

- Professional TTKBootstrap Theme
- Tab-Based Navigation
- Responsive Forms
- Interactive Tables
- Easy Record Selection
- Simple Navigation

---

## 🗄️ Database Integration

- MySQL Database Connectivity
- Automatic Data Retrieval
- Real-Time Record Updates
- Persistent Data Storage

---

# 🚀 Application Workflow

```text
Launch Application
        │
        ▼
Connect to MySQL
        │
        ▼
Library Dashboard
        │
 ┌──────┴───────────────┐
 │                      │
 ▼                      ▼
Books Module      Members Module
 │                      │
 ├── Add               ├── Add
 ├── Update            ├── Update
 ├── Delete            ├── Delete
 └── View              └── View
        │
        ▼
Database Updated
```

---

# 📋 Functional Modules

## 📚 Books Module

Manage all library books.

Information Stored:

- Book ID
- Title
- Author
- Genre
- Quantity

Operations:

- Add Book
- Update Book
- Delete Book
- View Books

---

## 👥 Members Module

Manage registered library members.

Information Stored:

- Member ID
- Name
- Email
- Phone Number

Operations:

- Add Member
- Update Member
- Delete Member
- View Members

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend Logic |
| Tkinter | GUI Framework |
| TTKBootstrap | Modern User Interface |
| MySQL | Database |
| mysql-connector-python | Database Connectivity |
| ttk Treeview | Data Display |
| MessageBox | Notifications |

---

# 📂 Project Structure

```text
Library_mng_py/
│
├── README.md
│
└── Library Management System/
    │
    ├── library manag sys.py
    └── library manag sys.sql
```

---

# 🗄️ Database

Database Name

```sql
library_db
```

Tables Used

```text
books
members
```

Books Table

- Book ID
- Title
- Author
- Genre
- Quantity

Members Table

- Member ID
- Name
- Email
- Phone Number

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/GamecraftRahul/Library_mng_py.git
```

---

## 2. Navigate to Project

```bash
cd Library_mng_py
```

---

## 3. Install Required Packages

```bash
pip install ttkbootstrap
pip install mysql-connector-python
```

---

## 4. Import Database

Import the SQL file into MySQL.

```text
library manag sys.sql
```

---

## 5. Configure Database

Open

```python
library manag sys.py
```

Modify the configuration:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_PASSWORD",
    "database": "library_db"
}
```

---

## 6. Run the Project

```bash
python "library manag sys.py"
```

---

# 📊 System Workflow

```text
Application
     │
     ▼
Database Connection
     │
     ▼
Library Dashboard
     │
 ┌───┴─────────────┐
 ▼                 ▼
Books          Members
 │                 │
 ▼                 ▼
CRUD           CRUD
 │                 │
 └──────┬──────────┘
        ▼
MySQL Database
```

---

# 🎯 Project Highlights

- Modern Bootstrap-Inspired Interface
- Two Independent Management Modules
- MySQL Database Integration
- CRUD Operations
- Interactive Data Tables
- Easy Record Editing
- Beginner-Friendly Code Structure
- Modular Design
- Responsive Desktop Interface

---

# 🔒 Current Features

- Input Validation
- Database Exception Handling
- Record Selection Validation
- Automatic Table Refresh
- Confirmation Messages
- Persistent Database Storage

---

# 🚀 Future Enhancements

## 🤖 Artificial Intelligence

- AI Book Recommendation System
- AI Reading Suggestions
- AI Book Popularity Prediction
- AI Library Analytics
- AI Chatbot Assistant
- Smart Book Search
- Voice-Based Search
- AI Report Generation

---

## ☁️ Cloud Features

- Cloud Database
- Multi-Library Synchronization
- Remote Access
- Cloud Backup
- Web Dashboard
- Mobile Application

---

## 📚 Advanced Library Features

- Book Borrowing System
- Book Return Management
- Due Date Tracking
- Fine Calculation
- Barcode Scanner Integration
- QR Code Support
- ISBN Lookup
- Book Reservation
- Digital Library
- Ebook Management

---

## 👥 User Features

- Student Login
- Librarian Login
- Admin Panel
- Role-Based Access Control
- Password Encryption
- Email Notifications
- SMS Notifications

---

## 📈 Reports

Generate:

- Available Books Report
- Borrowed Books Report
- Member Report
- Inventory Report
- Fine Collection Report
- Daily Activity Report
- Monthly Report
- PDF Export
- Excel Export

---

# 📚 Learning Outcomes

This project demonstrates practical knowledge of:

- Python Programming
- GUI Development
- TTKBootstrap Framework
- MySQL Integration
- CRUD Operations
- Event Handling
- Object-Oriented Programming
- Database Design
- Desktop Application Development

---

# 🌟 Future Scope

The project can be expanded into a complete **Digital Library ERP System** with:

- Online Library Portal
- RFID Integration
- Digital Membership Cards
- AI-Based Book Suggestions
- Student Portal
- Faculty Portal
- Mobile App
- Online Book Reservation
- Cloud Synchronization
- Analytics Dashboard
- Multi-Branch Library Support

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is developed for educational and academic purposes.

You are free to use, modify, and extend it for learning and research.

---

# 👨‍💻 Author

**Rahul Kulkarni**

Python Developer • Database Enthusiast • Desktop Application Developer • AI & Software Development Learner

---

# ⭐ Support

If you found this project helpful, please consider:

- ⭐ Star this repository
- 🍴 Fork the project
- 🛠️ Contribute improvements
- 📢 Share it with others

---

# 📬 Contact

For suggestions, feature requests, or bug reports, feel free to create an Issue or submit a Pull Request.

---

<p align="center">

## 📚 "A library is not just a collection of books—it is a gateway to knowledge."

### ⭐ Happy Coding! 🚀

</p>
