import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# False if not in os.environ because of casting above
DEBUG = env("DEBUG")

# To use Neon with Django, you have to create a Project on Neon and specify the project connection settings in your settings.py in the same way as for standalone Postgres.
DATABASES = {
    "default": env.db()
    # 'default': {
    #   'ENGINE': 'django.db.backends.postgresql',
    #   'NAME': 'neondb',
    #   'USER': '',
    #   'PASSWORD': '',
    #   'HOST': '',
    #   'PORT': '',
    # }
}
