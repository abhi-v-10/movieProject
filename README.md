# 🎬 MovieProject

MovieProject is a Django-based web application for managing a collection of movies and user accounts. It provides a user-friendly interface for adding, viewing, updating, and deleting movies, as well as user registration, login, and profile management. The project also exposes REST API endpoints for movie operations.

---

## 🚀 Features

- User registration and authentication (custom user model)
- Add, view, update, and delete movies
- User profile page with mobile number and age
- REST API endpoints for CRUD operations on movies
- Bootstrap-based responsive UI
- Admin interface for managing users and movies
- Demonstrates Django model relationships: One-to-One, One-to-Many, Many-to-Many

---

## 🗂️ Project Structure

```
movieProject/
│
├── movieProject/            # Django project settings and URLs
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── movieApp/                # Main application
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   │   ├── create_user.html
│   │   ├── get_movies.html
│   │   ├── home.html
│   │   ├── login_user.html
│   │   ├── post_movies.html
│   │   ├── profile.html
│   │   ├── update_movies.html
│   │   ├── relationships.html
│   │   ├── user_form.html
│   │   ├── watchlist.html
│   │   └── edit_user.html
│   │   
│   │      
│   │   
│   │ 
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── serializer.py
│
├── db.sqlite3               # SQLite database
└── manage.py                # Django management script
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd movieProject
```

### 2. Create a Virtual Environment

```sh
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```sh
pip install django djangorestframework djangorestframework-simplejwt
```

### 4. Apply Migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (for admin access)

```sh
python manage.py createsuperuser
```

### 6. Run the Development Server

```sh
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## 🖥️ Usage

- **Home Page:** `/`  
  Links to view and add movies.
- **Register:** `/create_user/`  
  Create a new user account.
- **Login:** `/login_user/`  
  Log in with your credentials.
- **Profile:** `/profile/`  
  View your profile (requires login).
- **Movies:**  
  - Add: `/post_movie/`
  - View: `/get_movie/`
  - Update: `/update_movie/<id>`
  - Delete: `/delete_movie/<id>`
  - Watchlist: `/watchlist/`
- **Add Related Data:** `/add_relations/`  
  Add movie details, production, and languages.

---

## 🔗 API Endpoints

All API endpoints use JSON and are implemented in [`movieApp/views.py`](movieApp/views.py).

| Method | Endpoint                        | Description                       |
|--------|---------------------------------|-----------------------------------|
| GET    | `/api_get_movie/`               | List all movies                   |
| POST   | `/api_post_movie/`              | Add a new movie                   |
| PUT    | `/api_update_movie/<id>`        | Update a movie                    |
| DELETE | `/api_delete_movie/<id>`        | Delete a movie                    |
| POST   | `/api_create_user/`             | Create a new user                 |
| POST   | `/api_register/`                | Register a new user (API)         |
| POST   | `/api_view_token/`              | Obtain JWT token                  |
| GET    | `/api_test_token/`              | Test JWT token validity           |
| POST   | `/api_logout/`                  | Logout and blacklist refresh token|
| POST   | `/create_token/`                | Obtain JWT token (SimpleJWT)      |
| POST   | `/refresh_token/`               | Refresh JWT token (SimpleJWT)     |
| POST   | `/refresh_custom_token/`        | Custom JWT token refresh          |

---

## 🧩 Models & Relationships

See [`movieApp/models.py`](movieApp/models.py).

- **Movies**: Main movie model with fields for name, language, year, genre, hero, heroine, rating, runtime, and relationships.
- **MovieDetails**: One-to-One with Movies (budget, collection).
- **Production**: One-to-Many with Movies (production house).
- **OtherLanguages**: Many-to-Many with Movies (other languages).
- **User**: Custom user model with `mobilenumber` and `age`.
- **Watchlist**: Contains user liked movies.

---

## 👤 Custom User Model

The project uses a custom user model (`User`) with additional fields:
- `mobilenumber`
- `age`

---

## 🛠️ Admin Panel

Access the Django admin at `/admin/` using your superuser credentials.  
Manage users and movies from the admin interface.

---

## 📦 Dependencies

- Django
- djangorestframework
- djangorestframework-simplejwt
- Bootstrap (via CDN for frontend)
- [requirements.txt](./requirements.txt)

---

## 📄 License

This project is for educational and personal use.

---

## 🙏 Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)