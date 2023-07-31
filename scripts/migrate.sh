#!/bin/sh

echo 'Executando migrações'

makemigrations.sh
python manage.py migrate --noinput