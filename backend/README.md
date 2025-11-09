# Сайт Лезгинских танцев
***
## Описание архитектуры эндпоинта
***
### GET /partners-gallery

Возвращает массив данных о компаниях-партнёрах, включая их логотипы и ссылки. Предназначено для отображения блока “Наши партнёры” на лендинге или где там ещё дизайнер нарисовал эти 12 логотипов в ряд.
#### Структура ответа
```json
[
    {
        "id": 1,
        "name": "Google",
        "image": "http://localhost:8000/media/partners/i_3.webp",
        "order": 100
    },
    {
        "id": 2,
        "name": "Yandex",
        "image": "http://localhost:8000/media/partners/i_4.webp",
        "order": 10
    }
]
```
#### Пояснения к полям
1) name - Название - идет в тег alt
2) image - ссылка на фотографию
3) order - сортировка (с бека идет уже в отсортированном виде)
***
### GET /our-projects/
Возвращает массив данных о наших проектах. Это для блока Проекты на главной странце
#### Структура ответа
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 7,
        "name": "выфа",
        "slug": "vyfa",
        "announcement": "testt",
        "image": "http://localhost:8000/media/our_projects/1.jpg"
    }
]
```
#### Пояснения к полям
1) name - Название - идет в тег alt
2) slug : "test"
3) description - Описание проекта
4) image - ссылка на фотографию
5) order - сортировка (с бека идет уже в отсортированном виде)
***
### GET /our-projects/{slug}/
Возвращает массив данных проекте. Это для детальной страницы
#### Структура ответа
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 7,
    "name": "выфа",
    "description": "testt",
    "image": "/media/our_projects/1.jpg"
}
```
#### Пояснения к полям
1) name - Название - идет в тег alt
2) description - Описание проекта
3) image - ссылка на фотографию

