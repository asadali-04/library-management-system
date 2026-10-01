# 📚 BookSphere — Library Management System

BookSphere is a modern web-based Library Management System built with Python and Streamlit. It provides a simple, interactive way to manage a small library’s books, members, borrowing activity, and returns from one dashboard.

## Live Application

🚀 [Open BookSphere](https://booksphere-library-asad-ali.streamlit.app/)

## About the Project

BookSphere was created to turn a terminal-based Python library project into a clean and user-friendly web application.

The project focuses on making daily library tasks easier. Instead of entering commands in a terminal, users can use a modern dashboard and visible navigation menu to manage their library.

The dashboard displays important information at a glance, including:

- Total book titles
- Total copies in the library
- Available copies
- Active members
- Recently added books
- Current borrowing status

## Features

- Modern dashboard interface
- Add new books with title, author, and copy count
- View and search the complete book collection
- Register library members
- View member details and borrowed books
- Issue books to members
- Return borrowed books
- Automatically update available book copies
- Store library information using JSON

## Development Note

The original Library Management System logic and terminal-based codebase were created by me.

I then used LLM-assisted development to help redesign the project as a modern Streamlit web application. The LLM support was used to improve the user interface, dashboard layout, styling, and to adapt the terminal workflow into an interactive web experience.

The project’s core idea, features, and original Python logic are my own work.

## Technologies Used

- Python
- Streamlit
- Pandas
- JSON
- HTML and CSS styling

## Project Structure

```text
library-management-system/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── library.json
```

## Data Storage

BookSphere stores books and member information in a `library.json` file.

> Note: JSON storage is suitable for learning and small projects. For a larger production library system, a cloud database such as PostgreSQL, Supabase, Firebase, or MongoDB would provide permanent shared storage.

## Application Pages

- Dashboard
- Add Book
- Books Collection
- Add Member
- Members
- Borrow Book
- Return Book

## Future Improvements

- User login for librarians and members
- Book cover images
- Due dates and overdue-book reminders
- Fine calculation
- Book categories and filters
- Database integration
- Downloadable reports
- Email notifications

## Author

Asad Ali  
Built with Python and Streamlit.
