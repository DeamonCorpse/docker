DEBUG = False
ALLOWED_HOSTS = "*"
DEFAULT_FROM_EMAIL = "email
REGISTRATION_OPEN = False
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = "465"
EMAIL_HOST_USER = "email"
EMAIL_HOST_PASSWORD = "secret"
EMAIL_USE_TLS = True
EMAIL_USE_VERIFICATION = True
SITE_ROOT = "http://localhost:8000"
SITE_NAME = "System Healthchecks"
BASE_URL = "IP"
CSRF_TRUSTED_ORIGINS = ["192.168.1.17"]
MASTER_BADGE_LABEL = "Systemchecks"
PING_ENDPOINT = SITE_ROOT + "/ping/"
PING_EMAIL_DOMAIN = "localhost"
PING_BODY_LIMIT = None
SLACK_CLIENT_ID = "ID"
SLACK_CLIENT_SECRET = "secret"