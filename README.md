# Weather App

A Django-based weather application that provides weather information through a web interface.

## Project Structure

```
weather/
├── build.sh                 # Build script
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── static/
│   └── style.css          # CSS styling
├── weather/                # Django project configuration
│   ├── __init__.py
│   ├── settings.py        # Django settings
│   ├── urls.py            # Project URL configuration
│   ├── asgi.py            # ASGI configuration
│   └── wsgi.py            # WSGI configuration
└── weather_app/            # Django application
    ├── __init__.py
    ├── models.py          # Database models
    ├── views.py           # View handlers
    ├── urls.py            # App URL routes
    ├── admin.py           # Admin configuration
    ├── apps.py            # App configuration
    ├── tests.py           # Test cases
    ├── migrations/        # Database migrations
    └── templates/
        └── index.html     # Main template
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd weather
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

## Running the Application

### Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

### Using the Build Script

Alternatively, you can use the provided build script:

```bash
./build.sh
```

## Features

- Weather information display
- Web-based interface
- SQLite database for data storage
- Responsive design with CSS styling

## Development

### Create a Superuser (for admin access)

```bash
python manage.py createsuperuser
```

Then navigate to `http://localhost:8000/admin` to access the Django admin panel.

### Make Database Migrations

After modifying models:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Tests

```bash
python manage.py test
```

## Requirements

All project dependencies are listed in `requirements.txt`. Key dependencies typically include:

- Django (web framework)
- Additional packages as specified in requirements.txt

## File Descriptions

- **manage.py** - Django command-line utility for administrative tasks
- **settings.py** - Django project settings and configuration
- **urls.py** - URL routing configuration
- **models.py** - Database models and schema definitions
- **views.py** - Business logic and request handlers
- **admin.py** - Django admin interface configuration
- **style.css** - Application styling
- **index.html** - Main template file

## License

[Add your license information here]

## Support

For issues or questions, please open an issue in the repository.
