#!/bin/bash

# Ejecutar migraciones
python manage.py makemigrations
python manage.py migrate

# Iniciar el servidor
python manage.py runserver