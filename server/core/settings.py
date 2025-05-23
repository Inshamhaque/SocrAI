from pathlib import Path
import os
from environ import Env
import dj_database_url

# 1. Setup base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Setup environment handler
env = Env()

# 3. Load .env file from the BASE_DIR
env.read_env(os.path.join(BASE_DIR, '.env'))

# 4. Confirm .env is being read
print("DEBUG: SECRET_KEY =", env('SECRET_KEY', default='NOT FOUND'))
print("DEBUG: OPENAI_API_KEY =", env('OPENAI_API_KEY', default='NOT FOUND'))

# 5. Now use the loaded values
SECRET_KEY = env('SECRET_KEY')
OPENAI_API_KEY = env('OPENAI_API_KEY')

# DEBUG mode
DEBUG = env.bool("DEBUG", default=True)

# 6. Allowed hosts
ALLOWED_HOSTS = ['*']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',  
    'allauth',
    'allauth.account',
    'allauth.socialaccount',  
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'api',
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases


#for development
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

#for production
DATABASES = {}
DATABASES['default'] = dj_database_url.parse(env('DATABASE_URL'))

CORS_ALLOW_ALL_ORIGINS = True #just for developemnt
CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_HTTPONLY = False
CSRF_USE_SESSIONS = False  
CSRF_COOKIE_SECURE = True 




# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin
    'django.contrib.auth.backends.ModelBackend',
    
    # allauth specific authentication methods
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Rest Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}

# Django Allauth settings
ACCOUNT_LOGIN_METHODS = {'email', 'username'} 
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'first_name*', 'last_name*', 'password1*', 'password2*']
ACCOUNT_UNIQUE_EMAIL = True  
ACCOUNT_EMAIL_VERIFICATION = 'optional'  


REST_SESSION_LOGIN = True


#change to smtp  
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True  
EMAIL_HOST_USER = env('EMAIL_ADDRESS')  
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')  
DEFAULT_FROM_EMAIL = f'SocrAI {env("EMAIL_ADDRESS")}'
ACCCOUNT_EMAIL_SUBJECT_PREFIX = ''


OPENAI_API_KEY = env('OPENAI_API_KEY')

ACCOUNT_USERNAME_BLACKLIST = ['admin', 'accounts', 'api']

REST_AUTH = {
    'REGISTER_SERIALIZER': 'api.serializers.CustomRegisterSerializer',
}