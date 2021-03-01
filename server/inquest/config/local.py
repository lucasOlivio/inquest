from inquest.config.common import *

DEBUG = True
AUTH_PASSWORD_VALIDATORS = []

# Testing
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
INSTALLED_APPS += ("django_nose",)
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
NOSE_ARGS = [
    BASE_DIR,
    "-s",
    "--nologcapture",
    "--with-coverage",
    "--with-progressive",
    "--cover-package=inquest",
]

# Mail
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
