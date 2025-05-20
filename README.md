# 🏨 **Nabroniroval** — Сервис бронирования отелей  

<img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" alt="Python 3.12">  
<img src="https://img.shields.io/badge/FastAPI-0.109.0-green?logo=fastapi" alt="FastAPI">  
<img src="https://img.shields.io/badge/PostgreSQL-16.0-blue?logo=postgresql" alt="PostgreSQL">  
<img src="https://img.shields.io/badge/Docker-Compose-orange?logo=docker" alt="Docker Compose">  

**Nabroniroval** — REST API для бронирования отелей, разработанный на современном стэке технологий.  

---

## 🚀 **Возможности**  
✅ **Бронирование номеров** с выбором дат и типов размещения  
✅ **JWT-авторизация** (регистрация, вход, верификация)  
✅ **Управление отелями и комнатами** (CRUD для администраторов)  
✅ **Кэширование через Redis** для ускорения ответов API  
✅ **Фоновые задачи через Celery**  
✅ **Масштабируемая архитектура** (Docker + Nginx)  

---

## 🛠 **Технологический стэк**  

| Категория       | Технологии                          |
|----------------|-----------------------------------|
| **Backend**    | Python 3.12, FastAPI, SQLAlchemy 2.0, Pydantic V2 |
| **База данных** | PostgreSQL 16, Alembic (миграции) |
| **Аутентификация** | JWT (access/refresh tokens)      |
| **Кэширование**  | Redis                             |
| **Асинхронные задачи** | Celery + Redis (брокер)       |
| **Тестирование**  | Pytest           |
| **Инфраструктура** | Docker, Docker Compose, Nginx    |

---

## 🐳 **Запуск через Docker**  

1. Склонируйте репозиторий:  
   ```bash
   git clone https://github.com/elmoons/Nabroniroval.git
   cd Nabroniroval
   ```

2. Настройте переменные окружения (см. `env-example`):  
   ```bash
   cp env-example .env
   ```

3. Запустите сервисы:  
   ```bash
   docker-compose up -d --build
   ```

4. API будет доступно на:  
   🔹 **http://localhost:7777** (FastAPI)  

---

## 📚 **Документация API**  

После запуска откройте:  
🔗 **Swagger UI**: http://localhost:7777/docs  
🔗 **Redoc**: http://localhost:7777/redoc  

---

## 🌟 **Особенности архитектуры**  
- **Слоистая структура** (API → Services → Repositories → Models)  
- **Асинхронные эндпоинты** (async/await)  
- **Модульные тесты** + интеграционные тесты API  

---

**Stars welcome!** ⭐️
