from .base import *
import dj_database_url

DEBUG = True

DATABASES = {
    'default': dj_database_url.config()
}


AWS_STORAGE_BUCKET_NAME = "harrisonliddiard"
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_PRELOAD_METADATA = True
STATICFILES_STORAGE = "storages.backends.s3boto.S3BotoStorage"
DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"
S3_URL = "http://%s.s3.amazonaws.com/" % AWS_STORAGE_BUCKET_NAME

STATIC_URL = S3_URL
MEDIA_URL = S3_URL
