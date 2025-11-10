
```markdown
# Backend API — Федеральная Лезгинская Национально-Культурная Автономия (ФЛНКА)

---

# Технологический стек backend

- Python 3.10
- Django 4.x
- Django REST Framework
- PostgreSQL
- django-parler (переводимые модели)
- Pillow (обработка фото)
- CKEditor5 (HTML редактор)
- Django CORS Headers
- Gunicorn / Uvicorn
- Nginx
- docker-compose (prod ready)
- drf-spectacular (OpenAPI Schema)
- Redis (дополнительно)

---

# Архитектура Django-проекта

src/
├── config/ # глобальные настройки, URL
├── about_us/
├── our_projects/
├── partners_gallery/
├── reports/
├── news/
├── content_list/
├── telegram_feed/
├── feedback_form/
├── media_library/
├── search/
└── utils/


---

# Детализация модулей

## about_us  
Модель хранения информации о ФЛНКА:

- заголовки
- подзаголовки
- HTML-текст
- фото/документы

Использует `TranslatableModel`.

## our_projects  
Сущность «Проект»:

- `name`
- `slug`
- `order`
- `image`
- `body` (HTML)
- `translations`

Поддерживает сортировку на уровне `Meta.ordering`.

## partners_gallery  
- логотип
- ссылочный переход
- сортировка по порядку
- alt-текст
- мультиязычное название

## reports  
Каждый отчёт:

- заголовок
- slug
- HTML-текст
- список фотографий
- дата публикации

Сильная нагрузка: HTML может достигать десятков кБ.

## telegram_feed  
Специальный endpoint, отдающий:

- `title`
- `image`
- `date`
- `link`

Используется фронтендом для отображения канала ФЛНКА.

## search  
Полнотекстовый поиск одновременно по:

- новостям
- проектам
- отчётам
- страницам
- медиа

Реализован через `icontains` + union на уровне QuerySet.

---

# Важные инженерные решения

### 1. Мультиязычные модели через django-parler  
Преимущество:

- переводы хранятся в отдельных таблицах
- API автоматически отдаёт текущую локаль
- сериализаторы DRF интегрированы прозрачно

### 2. Оптимизация медиа  
- Все фото хранятся в `ImageField`
- Возможны future upgrades: S3, CDN, cloud storage

### 3. Единая схема сортировки (order)  
Почти все списки используют поле `order`, благодаря чему фронт получает данные в нужном порядке.

### 4. Унифицированные ViewSet'ы  
Каждый модуль использует:

ListModelMixin
RetrieveModelMixin
GenericViewSet


Минимум лишней логики.

### 5. DRF Serializers → строгая типизация  
Сериализаторы описаны тщательно, что позволяет:

- гарантировать валидность
- формировать корректный OpenAPI schema
- документировать API для фронтенда

---

# Производительность

### SQL оптимизации  
- `select_related`
- `prefetch_related`
- `order_by`
- реплики БД можно включить при нагрузке

### Кеширование  
Поддержка через Redis (L2 cache).

---

# API Endpoints (примеры)

GET /api/about/
GET /api/our-projects/
GET /api/our-projects/<slug>/
GET /api/partners-gallery/
GET /api/reports/
GET /api/news/
GET /api/news/<slug>/
GET /api/telegram-feed/
GET /api/search/?q=<term>
POST /api/feedback-form/


---

# Безопасность

- CSRF защита
- CORS policy
- ограничение доменов
- sanitization HTML на уровне CKEditor
- возможность включения JWT слоя

---

# Готовность к продакшену

Проект можно деплоить:

- Docker + Gunicorn + Nginx
- Uvicorn (ASGI)
- PostgreSQL как основная БД
- Redis для кешей
- MinIO/S3 для медиа (опционально)

---

# Будущие расширения

- API для мобильного приложения ФЛНКА
- микросервисный вывод мероприятий
- автоматическая выгрузка документов в PDF
- модуль для регистрации участников форумов ФЛНКА
- интеграции с гос. системами (через единую точку API)

