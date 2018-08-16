#!/usr/bin/env bash

cd /root/retrospect

git pull

python manage.py collectstatic

python manage.py makemigrations

python manage.py migrate

