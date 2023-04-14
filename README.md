Учебный проект "API для социальной сети YaTube" 

Описание сервиса:

API для социальной сети YaTube позволяет использовать функционал сервиса, а именно: 
1) создавать, изменять и  удалять посты (могут только аутентифицированные пользователи)
2) получать список постов и конкретный пост по id
3) получать список групп и конкретную группу по id
4) создавать, измененять и  удалять коментарии (могут только аутентифицированные пользователи)
5) подписываться на других пользователей


Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

git clone git@github.com:SkogorevEduard/api_final_yatube.git
cd api_final_yatube
Cоздать и активировать виртуальное окружение:

python3 -m venv env
source venv/Scripts/activate
Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip
pip install -r requirements.txt
Выполнить миграции:

python manage.py migrate
Запустить проект:

python manage.py runserver

Примеры запросов:

Получение списка публикаций
GET /api/v1/posts/

Ответ:
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}

Создание, изменение публикации
POST /api/v1/posts/
PUT (PUTCH) /api/v1/posts/{id}/

Ответ:
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}

Получение публикации (либо ответ после создания/изменения)
GET /api/v1/posts/{id}/

Ответ:
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}

Получение списка комментариев одной публикации
GET /api/v1/posts/{post_id}/comments/

Ответ:
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]

Создание комментария к публикации
POST /api/v1/posts/{post_id}/comments/

Ответ:
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}

Получение списка групп
GET /api/v1/groups/

Ответ:
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]

Получение всех подписок пользователя, сделавшего запрос
GET /api/v1/follow/

Ответ:
[
  {
    "user": "string",
    "following": "string"
  }
]

Подписка пользователем на другого пользователя
POST /api/v1/follow/

Ответ:

{
  "user": "string",
  "following": "string"
}