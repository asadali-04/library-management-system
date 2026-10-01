import json
import random
import string
from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st


# ---------- App Setup ----------
st.set_page_config(
    page_title="BookSphere | Library Manager",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATABASE = Path("library.json")


# ---------- Styling ----------
st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at 10% 10%, #223b70 0%, transparent 25%),
                radial-gradient(circle at 90% 80%, #3e1e61 0%, transparent 30%),
                linear-gradient(135deg, #081224 0%, #101b33 55%, #121027 100%);
            color: #f6f8ff;
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #111d36 0%, #0a1223 100%);
            border-right: 1px solid rgba(255,255,255,0.10);
        }

        [data-testid="stSidebar"] * {
            color: #edf2ff !important;
        }

        .brand {
            font-size: 30px;
            font-weight: 800;
            letter-spacing: -1px;
            margin: 10px 0 2px;
        }

        .subtitle {
            color: #9eafd1;
            font-size: 14px;
            margin-bottom: 24px;
        }

        .page-title {
            font-size: 38px;
            font-weight: 800;
            letter-spacing: -1.3px;
            margin-bottom: 4px;
        }

        .page-description {
            color: #aebbd5;
            font-size: 16px;
            margin-bottom: 28px;
        }

        .metric-card {
            min-height: 150px;
            padding: 23px;
            border-radius: 22px;
            background: linear-gradient(145deg, #24395f, #162640);
            border: 1px solid rgba(255,255,255,0.12);
            box-shadow:
                12px 12px 24px rgba(0, 0, 0, 0.28),
                -5px -5px 16px rgba(109, 152, 255, 0.08);
            transition: transform 0.2s ease;
        }

        .metric-card:hover {
            transform: translateY(-5px);
        }

        .metric-icon {
            font-size: 28px;
            margin-bottom: 10px;
        }

        .metric-label {
            color: #b7c4df;
            font-size: 14px;
        }

        .metric-value {
            color: #ffffff;
            font-size: 34px;
            font-weight: 800;
            margin-top: 5px;
        }

        .section-card {
            padding: 24px;
            margin-top: 24px;
            border-radius: 22px;
            background: rgba(22, 38, 64, 0.76);
            border: 1px solid rgba(255,255,255,0.10);
            box-shadow: 10px 10px 25px rgba(0, 0, 0, 0.20);
        }

        .section-heading {
            font-size: 22px;
            font-weight: 700;
            margin-bottom: 4px;
        }

        .section-text {
            color: #aebbd5;
            margin-bottom: 16px;
        }

        .stButton button {
            border: none !important;
            border-radius: 12px !important;
            background: linear-gradient(135deg, #6d5dfc, #4e8df7) !important;
            color: white !important;
            font-weight: 700 !important;
            padding: 0.6rem 1rem !important;
            box-shadow: 0 7px 16px rgba(78, 141, 247, 0.25) !important;
        }

        .stButton button:hover {
            transform: translateY(-2px);
            filter: brightness(1.1);
        }

        .stTextInput input, .stNumberInput input, .stSelectbox div {
            border-radius: 10px !important;
        }

        .stDataFrame {
            border-radius: 14px;
            overflow: hidden;
        }

        hr {
            border-color: rgba(255,255,255,0.1);
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------- Data Functions ----------
def load_data():
    if DATABASE.exists():
        try:
            content = DATABASE.read_text(encoding="utf-8").strip()
            if content:
                loaded_data = json.loads(content)
                loaded_data.setdefault("books", [])
                loaded_data.setdefault("members", [])
                return loaded_data
        except (json.JSONDecodeError, OSError):
            pass

    return {"books": [], "members": []}


def save_data(data):
    DATABASE.write_text(json.dumps(data, indent=4), encoding="utf-8")


def generate_id(prefix="B"):
    code = "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
    return f"{prefix}-{code}"


def find_by_id(items, item_id):
    return next((item for item in items if item["id"] == item_id), None)


def show_metric(icon, label, value):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-icon">{icon}</div>
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


if "library" not in st.session_state:
    st.session_state.library = load_data()

data = st.session_state.library


# ---------- Sidebar ----------
with st.sidebar:
    st.markdown('<div class="brand">📚 BookSphere</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Modern Library Management</div>',
        unsafe_allow_html=True,
    )

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "➕ Add Book",
            "📖 Books Collection",
            "👤 Add Member",
            "👥 Members",
            "📤 Borrow Book",
            "📥 Return Book",
        ],
        label_visibility="collapsed",
    )

    st.divider()
    st.caption("© 2026 BookSphere")


# ---------- Dashboard ----------
if page == "🏠 Dashboard":
    st.markdown('<div class="page-title">Library Overview</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-description">Everything happening in your library, at a glance.</div>',
        unsafe_allow_html=True,
    )

    total_titles = len(data["books"])
    total_members = len(data["members"])
    total_copies = sum(book["total_copies"] for book in data["books"])
    available_copies = sum(book["available_copies"] for book in data["books"])
    borrowed_copies = total_copies - available_copies

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        show_metric("📚", "Book Titles", total_titles)
    with col2:
        show_metric("📦", "Total Copies", total_copies)
    with col3:
        show_metric("✅", "Available Now", available_copies)
    with col4:
        show_metric("👥", "Active Members", total_members)

    left, right = st.columns([1.5, 1])

    with left:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-heading">Recently Added Books</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-text">Your latest library additions.</div>', unsafe_allow_html=True)

        if data["books"]:
            recent_books = list(reversed(data["books"]))[:5]
            table_data = [
                {
                    "Title": book["title"],
                    "Author": book["author"],
                    "Available": f"{book['available_copies']} / {book['total_copies']}",
                }
                for book in recent_books
            ]
            st.dataframe(pd.DataFrame(table_data), use_container_width=True, hide_index=True)
        else:
            st.info("Your collection is empty. Add your first book to begin.")
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-heading">Circulation Status</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-text">Current book availability.</div>', unsafe_allow_html=True)

        if total_copies > 0:
            st.progress(available_copies / total_copies)
            st.write(f"**{available_copies}** copies available")
            st.write(f"**{borrowed_copies}** copies currently borrowed")
        else:
            st.info("No book copies available yet.")
        st.markdown("</div>", unsafe_allow_html=True)


# ---------- Add Book ----------
elif page == "➕ Add Book":
    st.markdown('<div class="page-title">Add a Book</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-description">Grow your collection with a new title.</div>', unsafe_allow_html=True)

    with st.form("add_book_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("Book Title", placeholder="For example: The Alchemist")
        with col2:
            author = st.text_input("Author Name", placeholder="For example: Paulo Coelho")

        copies = st.number_input("Number of Copies", min_value=1, value=1, step=1)
        submitted = st.form_submit_button("Add Book to Collection")

    if submitted:
        if not title.strip() or not author.strip():
            st.error("Please enter the book title and author name.")
        else:
            data["books"].append(
                {
                    "id": generate_id("B"),
                    "title": title.strip(),
                    "author": author.strip(),
                    "total_copies": copies,
                    "available_copies": copies,
                    "added_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
            save_data(data)
            st.success(f"“{title.strip()}” was added to your collection.")


# ---------- Books ----------
elif page == "📖 Books Collection":
    st.markdown('<div class="page-title">Books Collection</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-description">Browse and manage every book in your library.</div>', unsafe_allow_html=True)

    if not data["books"]:
        st.info("No books found. Add a book from the sidebar.")
    else:
        search = st.text_input("🔎 Search by title, author, or ID")

        filtered_books = [
            book for book in data["books"]
            if search.lower() in book["title"].lower()
            or search.lower() in book["author"].lower()
            or search.lower() in book["id"].lower()
        ]

        book_table = [
            {
                "ID": book["id"],
                "Title": book["title"],
                "Author": book["author"],
                "Total Copies": book["total_copies"],
                "Available": book["available_copies"],
                "Added On": book["added_on"],
            }
            for book in filtered_books
        ]

        st.dataframe(pd.DataFrame(book_table), use_container_width=True, hide_index=True)


# ---------- Add Member ----------
elif page == "👤 Add Member":
    st.markdown('<div class="page-title">Add a Member</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-description">Register a new reader in your library.</div>', unsafe_allow_html=True)

    with st.form("add_member_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", placeholder="Enter member name")
        with col2:
            email = st.text_input("Email Address", placeholder="member@example.com")

        submitted = st.form_submit_button("Register Member")

    if submitted:
        if not name.strip() or not email.strip():
            st.error("Please enter both name and email address.")
        else:
            data["members"].append(
                {
                    "id": generate_id("M"),
                    "name": name.strip(),
                    "email": email.strip(),
                    "borrowed": [],
                }
            )
            save_data(data)
            st.success(f"{name.strip()} is now a library member.")


# ---------- Members ----------
elif page == "👥 Members":
    st.markdown('<div class="page-title">Library Members</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-description">View members and their borrowed books.</div>', unsafe_allow_html=True)

    if not data["members"]:
        st.info("No members found. Add a member from the sidebar.")
    else:
        for member in data["members"]:
            with st.expander(f"👤 {member['name']}  •  {member['id']}"):
                col1, col2 = st.columns(2)
                col1.write(f"**Email:** {member['email']}")
                col2.write(f"**Borrowed books:** {len(member['borrowed'])}")

                if member["borrowed"]:
                    borrowed_table = [
                        {
                            "Book": book["title"],
                            "Book ID": book["book_id"],
                            "Borrowed On": book["borrowed_on"],
                        }
                        for book in member["borrowed"]
                    ]
                    st.dataframe(pd.DataFrame(borrowed_table), use_container_width=True, hide_index=True)
                else:
                    st.caption("No books borrowed currently.")


# ---------- Borrow Book ----------
elif page == "📤 Borrow Book":
    st.markdown('<div class="page-title">Borrow a Book</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-description">Issue an available book to a library member.</div>', unsafe_allow_html=True)

    available_books = [book for book in data["books"] if book["available_copies"] > 0]

    if not data["members"]:
        st.warning("Please add a member before issuing a book.")
    elif not available_books:
        st.warning("There are no available books to issue.")
    else:
        member_options = {
            f"{member['name']} ({member['id']})": member["id"]
            for member in data["members"]
        }
        book_options = {
            f"{book['title']} — {book['author']} ({book['available_copies']} available)": book["id"]
            for book in available_books
        }

        with st.form("borrow_book_form"):
            selected_member = st.selectbox("Select Member", list(member_options.keys()))
            selected_book = st.selectbox("Select Available Book", list(book_options.keys()))
            submitted = st.form_submit_button("Issue Book")

        if submitted:
            member = find_by_id(data["members"], member_options[selected_member])
            book = find_by_id(data["books"], book_options[selected_book])

            member["borrowed"].append(
                {
                    "book_id": book["id"],
                    "title": book["title"],
                    "borrowed_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
            book["available_copies"] -= 1
            save_data(data)
            st.success(f"“{book['title']}” was issued to {member['name']}.")


# ---------- Return Book ----------
elif page == "📥 Return Book":
    st.markdown('<div class="page-title">Return a Book</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-description">Receive a borrowed book back into the collection.</div>', unsafe_allow_html=True)

    members_with_books = [member for member in data["members"] if member["borrowed"]]

    if not members_with_books:
        st.info("There are no borrowed books waiting to be returned.")
    else:
        member_options = {
            f"{member['name']} ({member['id']})": member["id"]
            for member in members_with_books
        }

        selected_member_label = st.selectbox("Select Member", list(member_options.keys()))
        member = find_by_id(data["members"], member_options[selected_member_label])

        book_options = {
            f"{book['title']} ({book['book_id']})": index
            for index, book in enumerate(member["borrowed"])
        }

        with st.form("return_book_form"):
            selected_book_label = st.selectbox("Select Book to Return", list(book_options.keys()))
            submitted = st.form_submit_button("Return Book")

        if submitted:
            book_index = book_options[selected_book_label]
            returned_book = member["borrowed"].pop(book_index)

            original_book = find_by_id(data["books"], returned_book["book_id"])
            if original_book:
                original_book["available_copies"] += 1

            save_data(data)
            st.success(f"“{returned_book['title']}” has been returned successfully.")