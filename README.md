# 🎬 MovieDB - Complete Movie Management Platform

MovieDB is a comprehensive Django-based web application for managing movies, featuring user authentication, premium subscriptions, an AI chat assistant, and a full REST API.

🔗 **Live Demo:** [**abhishyanth.pythonanywhere.com**](https://abhishyanth.pythonanywhere.com)

-----

## ✨ Key Features

  - **User Management**: Custom user model with registration, login/logout, profile management, and social authentication (Google & GitHub).
  - **Movie CRUD**: Full create, read, update, and delete functionality for movies with comprehensive details.
  - **Advanced Search & Filtering**: Easily find movies by name, genre, language, release year, and production house.
  - **Watchlist System**: Users can "like" movies to add them to their personal, persistent watchlist.
  - **Premium Membership**: Stripe integration for paid subscriptions, unlocking exclusive content.
  - **AI Chat Assistant**: A Google Gemini-powered chatbot for movie-related queries, available to premium users.
  - **REST API**: A complete RESTful API with JWT authentication for all core functionalities.
  - **Responsive UI**: A modern, responsive interface built with Bootstrap.

-----

## 🛠️ Tech Stack

  - **Backend**: Django, Django REST Framework
  - **Authentication**: JWT (djangorestframework-simplejwt), Social Auth (OAuth2)
  - **Database**: SQLite (default), PostgreSQL (recommended)
  - **Payments**: Stripe
  - **AI**: Google Gemini
  - **Frontend**: HTML, CSS, Bootstrap 5
  - **Deployment**: PythonAnywhere (Demo)

-----

## 🗂️ Project Structure

```
movieProject/
│
├── movieProject/           # Django project settings
│   ├── settings.py
│   └── urls.py
│
├── movieApp/               # Main application
│   ├── models.py           # Database models
│   ├── views.py            # View logic and API endpoints
│   ├── serializer.py       # REST API serializers
│   ├── urls.py             # App URL routing
│   ├── forms.py
│   ├── pagination.py
│   ├── templates/
│   │   ├── ... (HTML templates)
│   └── admin.py
│
├── requirements.txt        # Python dependencies
└── manage.py               # Django management script
```

-----

## 🚀 Installation & Setup

### 1\. Clone the Repository

```bash
git clone <repository-url>
cd movieProject
```

### 2\. Create and Activate Virtual Environment

```bash
# Windows
python -m venv venv && venv\Scripts\activate

# macOS/Linux
python3 -m venv venv && source venv/bin/activate
```

### 3\. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4\. Configure Environment Variables

Create a `.env` file in the project root and add your keys:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3

STRIPE_SECRET_KEY=your-stripe-secret-key
STRIPE_PUBLISHABLE_KEY=your-stripe-publishable-key
GEMINI_API_KEY=your-gemini-api-key

GOOGLE_OAUTH_CLIENT_ID=your-google-oauth-client-id
GOOGLE_OAUTH_CLIENT_SECRET=your-google-oauth-client-secret
GITHUB_CLIENT_ID=your-github-client-id
GITHUB_CLIENT_SECRET=your-github-client-secret
```

### 5\. Run Migrations & Start Server

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

-----

## 🔌 REST API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api_register/` | Register a new user. |
| POST | `/create_token/` | Obtain JWT access/refresh tokens. |
| POST | `/refresh_token/` | Refresh an access token. |

### Movie Management

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api_get_movie/` | List all movies (with pagination). | No |
| POST | `/api_post_movie/` | Create a new movie. | Yes |
| PUT | `/api_update_movie/<id>` | Update an existing movie. | Yes |
| DELETE | `/api_delete_movie/<id>` | Delete a movie. | Yes |

-----

## 🗄️ Core Database Models

```python
# Custom User Model
class User(AbstractUser):
    mobilenumber = models.CharField(max_length=15, null=True)
    email = models.EmailField(unique=True)
    is_premium = models.BooleanField(default=False)

# Main Movie Model
class Movies(models.Model):
    name = models.CharField(max_length=250)
    language = models.CharField(max_length=100)
    rel_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    imdb_rating = models.FloatField()
    is_premium = models.BooleanField(default=False)
    # Relationships
    movie_details = models.OneToOneField(MovieDetails, null=True)
    production = models.ForeignKey(Production, null=True)
    other_languages = models.ManyToManyField(OtherLanguages, blank=True)
    liked_by = models.ManyToManyField(User, related_name="liked_movies")
```

-----

## 💌 Connect
Feel free to contact me via mail: v.abhishyanth118@gmail.com
