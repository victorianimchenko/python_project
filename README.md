# python_project

## migrations
python manage.py makemigrations
python manage.py migrate

## requirements
python -m pip install ..
python -m pip freeze > requirements.txt

## generate keys
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

## check setupds
python manage.py check
python manage.py check --database default

## run
python manage.py runserver