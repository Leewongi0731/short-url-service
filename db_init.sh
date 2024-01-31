#!/bin/bash
rm db.sqlite3
rm -f shortUrlServiceApp/migrations/0*.py
rm -f shortUrlServiceApp/migrations/__pycache__/*.pyc
python manage.py makemigrations
python manage.py migrate
