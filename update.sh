#!/usr/bin/env bash

cd /root/retrospect

mkdir backup

send=`date '+%Y-%m-%d-%H:%M:%S'`

tar -czvf  /root/retrospect/backup/media-${send}.tar.gz /root/retrospect/media/

git pull

python manage.py collectstatic

python manage.py makemigrations

python manage.py migrate
