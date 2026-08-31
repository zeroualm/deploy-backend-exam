# votre_projet/settings/production.py

from decouple import config
import dj_database_url
from .base import *

# ==============================================================================
# SÉCURITÉ
# ==============================================================================

DEBUG = False
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS',default='http://localhost:5173,http://127.0.0.1:5173').split(',')
ALLOWED_HOSTS = [host.strip() for host in config('DJANGO_ALLOWED_HOSTS', default='localhost').split(',')]

# ==============================================================================
# BASE DE DONNÉES
# ==============================================================================

DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        ssl_require=True
    )
}

# ==============================================================================
# FICHIERS STATIQUES (WHITENOISE)
# ==============================================================================

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'