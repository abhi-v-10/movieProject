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
│   │   └── update_movies.html
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
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```sh
pip install django djangorestframework
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

---

## 🔗 API Endpoints

- **List Movies:** `GET /api_get_movie/`
- **Add Movie:** `POST /api_post_movie/`
- **Update Movie:** `PUT /api_update_movie/<id>`
- **Delete Movie:** `DELETE /api_delete_movie/<id>`

All API endpoints use JSON and are implemented in [`movieApp/views.py`](movieApp/views.py).

---

## 👤 Custom User Model

The project uses a custom user model (`User`) with additional fields:
- `mobilenumber`
- `age`

See [`movieApp/models.py`](movieApp/models.py).

---

## 🛠️ Admin Panel

Access the Django admin at `/admin/` using your superuser credentials.  
Manage users and movies from the admin interface.

---

## 📦 Dependencies
- [requirements.txt](./requirements.txt)
- Django
- djangorestframework
- Bootstrap (via CDN for frontend)


---

## 📄 License

This project is for educational and personal use.

---

## 🙏 Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Bootstrap](https://getbootstrap.com/)
