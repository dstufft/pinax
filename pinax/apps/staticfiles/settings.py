import os.path
from django.conf import settings

ROOT = getattr(settings,
    'STATICFILES_ROOT',
    os.path.join(settings.PROJECT_ROOT, 'site_media', 'static'))
DIRS = getattr(settings,
    'STATICFILES_DIRS', ())
DIRNAMES = getattr(settings,
    'STATICFILES_MEDIA_DIRNAMES', ['media'])
PREPEND_LABEL_APPS = getattr(settings,
    'STATICFILES_PREPEND_LABEL_APPS', ('django.contrib.admin',))
