# 🎬 MovieDB - Complete Movie Management Platform

MovieDB is a comprehensive Django-based web application that provides a complete movie management system with user authentication, premium features, AI-powered chat assistance, payment integration, and REST API endpoints. Built with modern web technologies and featuring a beautiful, responsive UI.

---

## ✨ Key Features

### 🎯 Core Functionality
- **User Authentication & Management**: Custom user model with registration, login, logout, and profile management
- **Movie CRUD Operations**: Add, view, update, and delete movies with comprehensive details
- **Advanced Search & Filtering**: Search movies by name, language, genre, release year, and production
- **Pagination**: Multiple pagination styles (Page Number, Limit-Offset, Cursor-based)
- **Watchlist System**: Like/unlike movies and maintain personal watchlists
- **Relationship Management**: Handle complex movie relationships (One-to-One, One-to-Many, Many-to-Many)

### 🌟 Premium Features
- **Premium Membership**: Stripe-powered payment system for premium access
- **Exclusive Content**: Access to premium movies and early releases
- **AI Chat Assistant**: Powered by Google Gemini AI for movie-related queries
- **Enhanced User Experience**: Priority access and special features

### 🔧 Technical Features
- **REST API**: Complete RESTful API with JWT authentication
- **Social Authentication**: Google OAuth2 and GitHub OAuth integration
- **Custom Serializers**: Advanced data validation and serialization
- **Multiple Pagination Types**: Page Number, Limit-Offset, and Cursor pagination
- **Responsive Design**: Bootstrap-based modern UI with custom styling

---

## 🗂️ Project Structure

```
movieProject/
│
├── movieProject/                    # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                  # Project configuration
│   ├── urls.py                      # Main URL routing
│   └── wsgi.py
│
├── movieApp/                        # Main application
│   ├── __init__.py
│   ├── admin.py                     # Django admin configuration
│   ├── apps.py
│   ├── migrations/                  # Database migrations
│   ├── models.py                    # Database models
│   ├── views.py                     # View logic and API endpoints
│   ├── urls.py                      # App URL routing
│   ├── serializer.py                # REST API serializers
│   ├── forms.py                     # Django forms
│   ├── pagination.py                # Custom pagination classes
│   ├── templates/                   # HTML templates
│   │   ├── home.html               # Landing page
│   │   ├── create_user.html        # User registration
│   │   ├── login_user.html         # User login
│   │   ├── profile.html            # User profile
│   │   ├── edit_user.html          # Edit user details
│   │   ├── post_movies.html        # Add movies
│   │   ├── get_movies.html         # View movies with filters
│   │   ├── update_movies.html      # Edit movies
│   │   ├── watchlist.html          # User watchlist
│   │   ├── relationships.html      # Add movie relationships
│   │   ├── premium.html            # Premium upgrade page
│   │   ├── premium_movies.html     # Premium movies listing
│   │   ├── chat.html               # AI chat interface
│   │   ├── payment_success.html    # Payment success page
│   │   ├── payment_failed.html     # Payment failure page
│   │   └── user_form.html          # ModelForm example
│   └── tests.py
│
├── requirements.txt                 # Python dependencies
├── manage.py                       # Django management script
└── README.md                       # This file
```

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package installer)
- Git

### 1. Clone the Repository
```bash
git clone <repository-url>
cd movieProject
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the project root with the following variables:
```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True

# Database (SQLite by default)
DATABASE_URL=sqlite:///db.sqlite3

# Stripe Payment Configuration
STRIPE_SECRET_KEY=your-stripe-secret-key
STRIPE_PUBLISHABLE_KEY=your-stripe-publishable-key

# Google Gemini AI
GEMINI_API_KEY=your-gemini-api-key

# Social Authentication
GOOGLE_OAUTH_CLIENT_ID=your-google-oauth-client-id
GOOGLE_OAUTH_CLIENT_SECRET=your-google-oauth-client-secret
GITHUB_CLIENT_ID=your-github-client-id
GITHUB_CLIENT_SECRET=your-github-client-secret
```

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the application.

---

## 🎯 Core Features & Usage

### 🏠 Home Page (`/`)
- **Landing page** with navigation to all major features
- **Responsive design** with movie-themed background
- **Quick access** to view movies, add movies, and premium features

### 👤 User Management

#### Registration (`/create_user/`)
- Create new user accounts with validation
- Required fields: username, password, email, mobile number
- Email format validation and uniqueness check
- Mobile number validation (10-15 digits)

#### Login (`/login_user/`)
- Secure authentication system
- Session-based login
- Redirect to profile page after successful login

#### Profile Management (`/profile/`)
- View user information
- Access to edit profile and logout options

#### Edit Profile (`/edit_user/`)
- Update mobile number and display name
- Form validation and error handling

### 🎬 Movie Management

#### Add Movies (`/post_movie/`)
- **Comprehensive movie form** with all details
- **Validation**: IMDB rating (0-10), runtime (positive), required fields
- **Premium toggle**: Mark movies as premium content
- **Relationship fields**: Production house, other languages, movie details

#### View Movies (`/get_movie/`)
- **Advanced filtering** by:
  - Movie name (partial match)
  - Language
  - Genre
  - Release year
  - Production house
- **Pagination**: 5 movies per page
- **Like/Unlike functionality**: Add movies to watchlist
- **Premium content filtering**: Only non-premium movies shown to regular users

#### Update Movies (`/update_movie/<id>`)
- **Edit existing movies** with pre-populated forms
- **Validation**: Same as add movie form
- **Relationship management**: Update production, languages, details

#### Delete Movies (`/delete_movie/<id>`)
- **Secure deletion** with confirmation
- **Permission-based**: Only authenticated users can delete

### 📋 Watchlist System (`/watchlist/`)
- **Personal movie collection**: View all liked movies
- **Time tracking**: Shows when movies were added
- **Easy management**: Remove movies from watchlist
- **Responsive design**: Mobile-friendly interface

### 🔗 Relationship Management (`/add_relations/`)
- **Movie Details**: Add budget and collection information
- **Production Houses**: Create new production companies
- **Other Languages**: Add multiple language options for movies

---

## 🌟 Premium Features

### 💳 Premium Membership
- **Stripe Integration**: Secure payment processing
- **Pricing**: ₹50/month (₹5000 in paise)
- **Features unlocked**:
  - Access to premium movies
  - AI chat assistant
  - Early access to new releases
  - Special offers and discounts

### 🎬 Premium Movies (`/premium_movies/`)
- **Exclusive content**: Movies marked as premium
- **Access control**: Only premium users can view
- **Enhanced experience**: Better quality and exclusive releases

### 🤖 AI Chat Assistant (`/gemini_ai/`)
- **Powered by Google Gemini**: Advanced AI model
- **Movie-focused**: Specialized in movie-related queries
- **Chat history**: Persistent conversation history
- **Premium access**: Only available to premium users
- **Real-time responses**: Instant AI-powered answers

### 💰 Payment Processing
- **Success Page** (`/payment_success/`): Confirms premium activation
- **Failure Page** (`/payment_failed/`): Handles payment errors
- **Automatic activation**: Premium status updated immediately

---

## 🔌 REST API Endpoints

### Authentication Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api_register/` | Register new user | No |
| POST | `/api_view_token/` | Obtain JWT token | No |
| GET | `/api_test_token/` | Validate JWT token | Yes |
| POST | `/api_logout/` | Logout and blacklist token | Yes |
| POST | `/create_token/` | SimpleJWT token creation | No |
| POST | `/refresh_token/` | Refresh JWT token | No |
| POST | `/refresh_custom_token/` | Custom token refresh | No |

### Movie Management API
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api_get_movie/` | List all movies | No |
| POST | `/api_post_movie/` | Create new movie | Yes |
| PUT | `/api_update_movie/<id>` | Update movie | Yes |
| DELETE | `/api_delete_movie/<id>` | Delete movie | Yes |

### Pagination API
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api_limit_offset/` | Limit/Offset pagination | No |
| GET | `/api_page_number/` | Page number pagination | No |
| GET | `/api_cursor/` | Cursor-based pagination | No |

### User Management API
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api_create_user/` | Create user via API | No |

---

## 🗄️ Database Models

### User Model (Custom)
```python
class User(AbstractUser):
    display_name = models.CharField(max_length=150, blank=True)
    mobilenumber = models.CharField(null=True, max_length=15)
    email = models.EmailField(unique=True, blank=True, null=True)
    is_premium = models.BooleanField(default=False)
```

### Movie Models
```python
class Movies(models.Model):
    name = models.CharField(max_length=250)
    language = models.CharField(max_length=100)
    rel_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    hero = models.CharField(max_length=100)
    heroine = models.CharField(max_length=100)
    imdb_rating = models.FloatField()
    runtime = models.IntegerField()
    movie_details = models.OneToOneField(MovieDetails, null=True)
    production = models.ForeignKey(Production, null=True)
    other_languages = models.ManyToManyField(OtherLanguages, blank=True)
    liked_by = models.ManyToManyField(User, related_name="liked_movies")
    is_premium = models.BooleanField(default=False)
```

### Relationship Models
- **MovieDetails**: One-to-One with Movies (budget, collection)
- **Production**: One-to-Many with Movies (production house)
- **OtherLanguages**: Many-to-Many with Movies (additional languages)
- **Watchlist**: User-movie relationship with timestamps

---

## 🔐 Security Features

### Authentication & Authorization
- **JWT Tokens**: Secure token-based authentication
- **Session Management**: Django's built-in session handling
- **Permission Classes**: REST framework permission system
- **Social Authentication**: Google OAuth2 and GitHub OAuth

### Data Validation
- **Form Validation**: Client and server-side validation
- **Serializer Validation**: API data validation
- **Model Validation**: Database-level constraints
- **Custom Validators**: Email format, mobile number format

### Payment Security
- **Stripe Integration**: PCI-compliant payment processing
- **Secure Keys**: Environment variable management
- **Error Handling**: Graceful payment failure handling

---

## 🎨 UI/UX Features

### Design System
- **Bootstrap 5**: Modern responsive framework
- **Custom Styling**: Movie-themed design with gradients
- **Responsive Design**: Mobile-first approach
- **Interactive Elements**: Hover effects and animations

### User Experience
- **Intuitive Navigation**: Clear menu structure
- **Form Validation**: Real-time error feedback
- **Loading States**: Visual feedback for actions
- **Success/Error Messages**: Clear user communication

### Visual Elements
- **Movie-themed Background**: Cinematic design
- **Color Scheme**: Red and black theme (Netflix-inspired)
- **Typography**: Modern, readable fonts
- **Icons**: Bootstrap Icons integration

---

## 🚀 Deployment

### Production Considerations
1. **Environment Variables**: Secure configuration management
2. **Database**: Consider PostgreSQL for production
3. **Static Files**: Configure static file serving
4. **Security**: Set DEBUG=False and configure ALLOWED_HOSTS
5. **SSL**: Enable HTTPS for payment processing

### Recommended Hosting
- **Heroku**: Easy deployment with PostgreSQL
- **DigitalOcean**: VPS with full control
- **AWS**: Scalable cloud infrastructure
- **Railway**: Modern deployment platform

---

## 🧪 Testing

### Manual Testing
- User registration and authentication
- Movie CRUD operations
- Premium feature access
- Payment processing
- API endpoint functionality

### Automated Testing
```bash
python manage.py test
```

---

## 📦 Dependencies

### Core Dependencies
- **Django 5.2.1**: Web framework
- **djangorestframework 3.16.0**: REST API framework
- **djangorestframework-simplejwt**: JWT authentication
- **stripe**: Payment processing
- **google-generativeai**: AI chat integration
- **python-decouple**: Environment configuration

### Development Dependencies
- **asgiref 3.8.1**: ASGI utilities
- **sqlparse 0.5.3**: SQL parsing
- **tzdata 2025.2**: Timezone data

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Django Community**: For the excellent web framework
- **Bootstrap Team**: For the responsive CSS framework
- **Stripe**: For secure payment processing
- **Google**: For Gemini AI integration
- **Open Source Community**: For various supporting libraries

---

## 📞 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

---

**MovieDB** - Your complete movie management solution! 🎬✨