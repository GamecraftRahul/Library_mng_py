-- -------------------------------
-- Create Database
-- -------------------------------
CREATE DATABASE IF NOT EXISTS library_db;
USE library_db;

-- -------------------------------
-- Table: Books
-- -------------------------------
CREATE TABLE IF NOT EXISTS books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    quantity INT DEFAULT 1
);

-- -------------------------------
-- Table: Members
-- -------------------------------
CREATE TABLE IF NOT EXISTS members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20)
);

-- -------------------------------
-- Table: Transactions
-- -------------------------------
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    borrow_date DATE NOT NULL,
    return_date DATE,
    status ENUM('borrowed', 'returned') DEFAULT 'borrowed',
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

-- -------------------------------
-- Sample Data: Books
-- -------------------------------
INSERT INTO books (title, author, genre, quantity) VALUES
('Harry Potter and the Sorcerer''s Stone', 'J.K. Rowling', 'Fantasy', 5),
('The Alchemist', 'Paulo Coelho', 'Adventure', 3),
('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 4),
('1984', 'George Orwell', 'Dystopian', 6);

-- -------------------------------
-- Sample Data: Members
-- -------------------------------
INSERT INTO members (name, email, phone) VALUES
('Alice Johnson', 'alice@example.com', '1234567890'),
('Bob Smith', 'bob@example.com', '0987654321'),
('Charlie Brown', 'charlie@example.com', '1112223333');

-- -------------------------------
-- Sample Data: Transactions
-- -------------------------------
INSERT INTO transactions (book_id, member_id, borrow_date, status) VALUES
(1, 1, '2025-10-01', 'borrowed'),
(2, 2, '2025-10-05', 'returned'),
(3, 3, '2025-10-10', 'borrowed');
