from pymongo import MongoClient

MONGO_CLIENT = MongoClient('mongodb://localhost:27017/')
MONGO_DB = MONGO_CLIENT['octofit_db']

# Ensure INSTALLED_APPS is initialized
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'octofit_tracker.apps.OctofitTrackerConfig',
    'rest_framework',
    'corsheaders',  # Ensure this appears only once
]

# Ensure MIDDLEWARE is initialized
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Add CORS headers middleware
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

# Allow all origins for now (adjust as needed for production)
CORS_ALLOW_ALL_ORIGINS = True

# Allow all hosts
ALLOWED_HOSTS = ['*']

# Ensure PORT is an integer for MongoDB connection
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,  # Set PORT as an integer
    }
}

# Add TEMPLATES configuration for Django admin
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Set DEFAULT_AUTO_FIELD to avoid warnings
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Enable CORS
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'DELETE',
    'OPTIONS',
]
CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
]

# Allow all hosts
ALLOWED_HOSTS = ['*']