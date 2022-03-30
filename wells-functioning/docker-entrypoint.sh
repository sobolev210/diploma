#!/bin/bash
# when using build . in docker-compose
sleep 10
pip install -r requirements.txt
python manage.py makemigrations && \
python manage.py migrate && \
python manage.py runserver 0.0.0.0:8000
