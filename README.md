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

## deploy.zip

@'
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path.cwd()

excluded_dirs = {
    ".venv", ".git", ".idea", ".vscode",
    "__pycache__", "staticfiles"
}

excluded_files = {
    ".env", "db.sqlite3", "deploy.zip"
}

with ZipFile("deploy.zip", "w", ZIP_DEFLATED) as archive:
    for file in root.rglob("*"):
        relative = file.relative_to(root)

        if not file.is_file():
            continue

        if any(part in excluded_dirs for part in relative.parts):
            continue

        if file.name in excluded_files or file.suffix == ".pyc":
            continue

        archive.write(file, relative)

print("deploy.zip created successfully!")
'@ | python -
