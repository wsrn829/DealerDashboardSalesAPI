web: gunicorn sales_project.wsgi:application -c gunicorn.conf.py

worker: celery -A sales_project worker --loglevel=info

beat: celery -A sales_project beat --loglevel=info