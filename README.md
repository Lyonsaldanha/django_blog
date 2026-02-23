# Django Blog

A minimalist blog application built with Django, featuring user authentication and full CRUD functionality.

## Features
- **Authentication**: Sign up, Login, and Logout.
- **CRUD Operations**: Create, Read, Update, and Delete blog posts.
- **Author Control**: Automatic author assignment and restricted editing/deletion (where implemented in templates).

## Tech Stack
- **Framework**: Django
- **Database**: SQLite
- **Configuration**: python-dotenv

## Setup
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd django_blog
   ```
2. **Setup Virtual Environment**:
   ```bash
   python -m venv env
   source env/Scripts/activate  # Windows
   ```
3. **Install Dependencies**:
   ```bash
   pip install django python-dotenv
   ```
4. **Environment Variables**:
   Create a `.env` file in the root:
   ```env
   DJANGO_SECRET_KEY=your-secret-key
   ```
5. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```
6. **Start Server**:
   ```bash
   python manage.py runserver
   ```

## Testing
Run the test suite using:
```bash
python manage.py test
```
