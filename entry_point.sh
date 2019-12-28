#!/bin/sh

cd /home/ubuntu/src/app

python3 manage.py makemigrations
python3 manage.py migrate

echo "Django is ready.";
python3 manage.py runserver 0.0.0.0:8000
