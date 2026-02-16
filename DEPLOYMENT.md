# Esearch Website Deployment & Usage Guide

## Project Overview
Unveil the "Esearch" enterprise image search API platform website.
Built with Django 5.0, this project features:
- **Bilingual Support**: English (default) & Persian (RTL).
- **Theme System**: Dark/Light mode with local storage persistence.
- **Enterprise Design**: Minimal, orange-accented corporate aesthetic.
- **SEO Optimized**: Meta tags, Sitemap, Robots.txt, and I18N URLs.
- **Contact Integration**: Dual forms for General Contact and API Requests.

## Prerequisites
- Python 3.10+
- Pip
- Virtual Environment (recommended)

## 1. Setup & Installation
```bash
# Data encryption
python -m venv venv
# Activate (Windows)
.\venv\Scripts\activate
# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 2. Database Initialization
```bash
python manage.py makemigrations core
python manage.py migrate
```

## 3. Translation Setup (Important)
To generate the translation files for Persian:

```bash
# Create the locale directory if it doesn't exist
mkdir locale

# Update message files
django-admin makemessages -l fa

# ... Open locale/fa/LC_MESSAGES/django.po and translate the strings ...

# Compile messages
django-admin compilemessages
```
*Note: You need `gettext` installed on your system for `makemessages` to work.*

## 4. Static Files
For production, collect static files:
```bash
python manage.py collectstatic
```

## 5. Running the Development Server
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/

## 6. Admin Panel
Create a superuser to access submitted forms:
```bash
python manage.py createsuperuser
```
Access at http://127.0.0.1:8000/admin/

## 7. Production Settings
In `esearch_project/settings.py`, update for production:
- `DEBUG = False`
- `ALLOWED_HOSTS = ['yourdomain.com']`
- `CSRF_TRUSTED_ORIGINS = ['https://yourdomain.com']`
- Configure a real database (PostgreSQL recommended).
- Use a production server like Gunicorn + Nginx.

## File Structure
- `core/`: Main app logic (views, models, forms).
- `templates/`: HTML templates (Base, Home, About, Docs, Contact).
- `static/css/`: Stylesheets.
- `locale/`: Translation files.

## Features
- **URL Structure**: `/en/` and `/fa/` prefixes.
- **Theme**: Automatic system detection + Manual toggle.
- **SEO**: Dynamic meta tags in `base.html`.
