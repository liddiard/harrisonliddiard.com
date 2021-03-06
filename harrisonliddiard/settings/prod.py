from .base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config()
}


AWS_STORAGE_BUCKET_NAME = "harrisonliddiard"
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_PRELOAD_METADATA = True
DEFAULT_FILE_STORAGE = 'portfolio.s3utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'portfolio.s3utils.StaticRootS3BotoStorage'
S3_URL = "http://%s.s3.amazonaws.com/" % AWS_STORAGE_BUCKET_NAME


STATIC_URL = S3_URL + 'static/'
MEDIA_URL = S3_URL + 'media/'
