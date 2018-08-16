#!/usr/bin/env bash


mkdir /root/backup

send=`date '+%Y%m%d-%H%M%S'`

tar -czvf  /root/backup/media-${send}.tar.gz /root/retrospect/media/

cd /root/retrospect

git fetch --all

git reset --hard origin/master

git pull

python manage.py collectstatic

python manage.py makemigrations

python manage.py migrate
