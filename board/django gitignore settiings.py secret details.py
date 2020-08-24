DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'appjo$87-f5qf_=(yoh$=b#-^s!8v!onixfki=6ep)m-4_fgz@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
