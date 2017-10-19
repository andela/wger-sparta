#!/usr/bin/env python
from django.conf import settings
from django.core.cache import cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}

settings.configure(CACHES=CACHES) # include any other settings you might need

cache.clear()
print ("***", "cache cleared successfully", "***")
