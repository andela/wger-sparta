release: invoke create-settings
release: invoke bootstrap-wger
release: python manage.py migrate 
web: gunicorn wger.wsgi:application
