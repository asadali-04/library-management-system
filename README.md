# 📚 BookSphere — Library Management System

A modern Library Management System built with Python and Streamlit.

BookSphere helps librarians manage books, members, borrowing, and returns through a clean interactive dashboard.

## Features

- Modern dashboard with book and member statistics
- Add and view books
- Register and view library members
- Borrow available books
- Return borrowed books
- Search the book collection
- JSON-based local data storage
- Responsive Streamlit interface with a modern visual design

## Project Structure

```text
library-management-system/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── library.json
```

## Installation

Clone this repository:

```bash
git clone https://github.com/YOUR-USERNAME/library-management-system.git
cd library-management-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## Requirements

- Python 3.9 or newer
- Streamlit
- Pandas

## Deployment

This project can be deployed using Streamlit Community Cloud.

1. Push this project to a GitHub repository.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io).
3. Sign in using GitHub.
4. Click **Create app**.
5. Select your repository and choose `app.py` as the main file.
6. Click **Deploy**.

## Data Storage

The project stores book and member data in `library.json`.

> Note: Local JSON storage is suitable for learning and testing. For a production application, use a cloud database such as PostgreSQL, Supabase, Firebase, or MongoDB so data remains available after redeployment.

## Screens Included

- Dashboard
- Add Book
- Books Collection
- Add Member
- Members
- Borrow Book
- Return Book

## Author

Asad Ali
Built with Python and Streamlit.
