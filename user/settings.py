LOGIN_REDIRECT_URL = 'userapp:dashboard'
LOGIN_URL= 'login'
LOGOUT_URL= 'logout'

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = str('templates/emails'.joinpath('sent_emails'))