#!/bin/bash

# Ejecutar migraciones
python manage.py makemigrations
python manage.py migrate

# Crear superusuario (no recomendado)
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'fprios112@gmail.com', 'Fer123456*')" | python manage.py shell

# Iniciar el servidor
python manage.py runserver 0.0.0.0:8000