#!/bin/bash

# Ejecutar migraciones
python manage.py makemigrations
python manage.py migrate


# Iniciar el servidor
python manage.py runserver 0.0.0.0:8000