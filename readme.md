# DRF Books API

A Django-based REST API for managing books, user authentication, and MongoDB integration. This project includes features like registering users, logging in, managing books, and secure access using JWT authentication.

## Features

- User registration, login, and logout
- JWT-based authentication for secure API endpoints
- CRUD operations for managing books
- MongoDB integration for storing data

---

## Requirements

- Python 3.12+
- MongoDB
- Django 5.1+
- Virtual environment (optional)

---

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/drf-books-api.git
   cd drf-books-api

2. **Create a Virtual Environment**:
    ```bash
    python -m venv .myenv
    source .myenv/bin/activate  # Linux/macOS
    .myenv\Scripts\activate     # Windows
    ```

3. **Install Dependencies**:
  ```bash
    pip install -r requirements.txt
  ```
4. **Set Up Environment Variables: Create a .env file in the project root with the following variables**:
  ```plaintext
    DB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<database>?retryWrites=true&w=majority
    DB_NAME=books_database
    SECRET_KEY=your_secret_key
  ```
5. **Run Migrations**:
  ```bash
    python manage.py makemigrations
    python manage.py migrate
  ```
6. **Start the Server**:
  ```bash
    python manage.py runserver
  ```

# API Endpoints

## Authentication
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Log in and retrieve a JWT token
- `POST /api/auth/logout/` - Log out the user (client-side token removal)
## Books
- `GET /api/books/` - List all books
- `POST /api/books/create/` - Add a new book (requires JWT token)
- `PUT /api/books/<book_id>/update/` - Update a book (requires JWT token)
- `DELETE /api/books/<book_id>/delete/`- Delete a book (requires JWT token)

# Example Requests
## Register a User
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "password123"}'
```
## Login and Retrieve a Token
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "password123"}'
```
## Add a New Book
```bash
curl -X POST http://localhost:8000/api/books/create/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_JWT_TOKEN" \
     -d '{"title": "Sample Book", "author": "Author Name", "isbn": "1234567890"}'
```

# Project structure

```
drf_books_api/
├── books/
│   ├── models/
│   │   ├── books.py
│   │   ├── reviews.py
│   │   ├── auth/
│   │       ├── users.py
│   ├── views/
│       ├── books.py
│       ├── auth.py
├── drf_books_api/
│   ├── settings.py
│   ├── urls.py
├── manage.py
├── requirements.txt
├── .env
└── .gitignore
```