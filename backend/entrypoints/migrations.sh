#!/bin/bash

echo "Старт миграций"
python manage.py migrate
echo "Миграции успешно выполнены"