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

Возможности кратко:


  фильтры на главной, вывод записей, добавлений записей.
  Редактирование и удаление любой записи или модели
  На странице справочники это возможно сделать, выбрал соответствующую модель

  
  <img width="393" height="245" alt="image" src="https://github.com/user-attachments/assets/77f03b46-5e99-4485-b243-1f7ddd08bbf6" />

  
  <img width="1171" height="303" alt="image" src="https://github.com/user-attachments/assets/f9a66639-2f96-4f89-9023-c6baf9130481" />  

Как запустить локально:
1. Склонировать проект: git clone https://github.com/valera122333/dds_project
2. Собрать и запустить контейнеры:
   docker-compose up --build
3.Поменяйте в настройках хост, иначе не запустится
   ALLOWED_HOSTS = ["*"]
4. Сайт будет доступен на: http://localhost:8000
5. Логин и пароль от админки.
   admin
   admin
   
Комментарий: при удалении любой из моделей в справочнике, я не стал удалять связанные все с этими моделями записи, решил оставить, заполнил поля None.
Требования по ТЗ в этом моменте не было, решил сделать так чтобы записи не удалялись. Если есть необходимость, могу переделать.


