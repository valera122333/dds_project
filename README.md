Проект: DDS Project
<img width="2559" height="595" alt="image" src="https://github.com/user-attachments/assets/8532b082-7ed0-49b5-94b0-76293b740d44" />

Ссылка на сайт: https://ddsproject-production.up.railway.app

Стек:
- Python 3.11
- Django 4.x
- PostgreSQL 15
- Gunicorn
- Docker + Docker Compose
- Railway (хостинг)
- Htmls css js
Структура проекта:
<img width="488" height="1137" alt="image" src="https://github.com/user-attachments/assets/9b4dac02-43b3-487f-be1a-cbd73874af32" />

Как запустить локально:
1. Склонировать проект: git clone https://github.com/valera122333/dds_project
2. Собрать и запустить контейнеры:
   docker-compose up --build
3.Поменяйте в настройках хост, иначе не запустится
   ALLOWED_HOSTS = ["*"]
4. Сайт будет доступен на: http://localhost:8000


