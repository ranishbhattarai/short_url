# Short URL Generator

This is a Django-based URL shortener application that converts long URLs into short, shareable links. This app includes user authentication, click tracking, and cryptographically secure key generation.

# Hello from Developer
Hey My name is Ranish Bhattarai. Let me give you full brief description about my Project.

### **Custom User Model**
- You can find a customUser model at accounts/model.py **why?**
Cause once a project grow you often need a extra user fields like phonenumber, email, image, student id etc.
- The customUser model will help you to modify/add fields easily instead of that painful migration in future cause django default User is very hard to modify

### **Cryptographically Secure instead of Base62**
- I have used Python's `secrets` module to generate unpredictable, cryptographically secure short keys of length 6:

```python
def generate_secure_short_key(length=6):
    from slinks.models import ShortLink

    while True:
        characters = string.ascii_letters + string.digits
        key = ''.join(secrets.choice(characters) for _ in range(length))

        # check if key already exists in the database
        if not ShortLink.objects.filter(short_key=key).exists():
            return key
```

**Why?**:
- 62^6 ≈ I can create 56.8 billion possible combinations of short_url
* The short_link will be unpredictable and non-enumerable that means it is secured and can't be guessed
+ Protection against sequential guessing attacks which can cause in Base_62 Encoding
+ It is safer for Sensative/Private links

**Note**
- I have added a while True loop to stop collision of same short_links on slinks/utils.py
+ It generates a random key, if already exsist in the databse, and returns only if it doesn't exsist, otherwise regenrates the short_link key

** It helped me to prevent IntegrityError crashes and ensure every short_url get a unique key **


### **Frontend**
+ I have used HTML with Tailwind CSS to build a responsive UI. As Tailwind CSS is Mobile First Approach it was a best for the User Friendy and Responsive desgin for my project. With built in templates and large CSS library it was easy to build the frontend and to achive responsive UI


## Technology Stack

- **Backend**: Django 6.0.1
- **Database**: SQLite3 (default, can be configured for PostgreSQL/MySQL)
- **Frontend**: HTML, CSS (Tailwind CSS)
- **Python**: 3.14.2

## Installation

### Prerequisites

- Python 3.8 or higher
-uv (fast Python package and project manager)
-pip(python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   ```

2. **Create a virtual environment**
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   uv pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and navigate to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Project Structure

```
jr_dev_task/
├── accounts/           # User authentication app
│   ├── models.py      # Custom user model
│   ├── views.py       # Registration views
│   ├── forms.py       # User registration forms
│   └── urls.py        # Account-related URLs
├── slinks/            # Short link app
│   ├── models.py      # ShortLink model
│   ├── views.py       # Link CRUD views
│   ├── forms.py       # ShortLink forms
│   ├── utils.py       # Secure key generation
│   └── urls.py        # Link-related URLs
├── core/              # Project settings
│   ├── settings.py    # Django settings
│   └── urls.py        # Main URL configuration
├── templates/         # HTML templates
├── db.sqlite3         # SQLite database
├── manage.py          # Django management script
└── requirements.txt   # Python dependencies
```

## Configuration

### Database
By default, the project uses SQLite. To use PostgreSQL or MySQL, update `DATABASES` in [core/settings.py](core/settings.py):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
## License

Copyright (c) 2026 Ranish Bhattarai.

## Contact

For questions or support, please contact the repository maintainer.

---

