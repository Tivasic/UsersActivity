## Запуск
1. Установить зависимости: 

```
pip install -r requirements.txt
```

2. В database/db.py изменить данные подключения к БД.

3. Настроить авто миграция:

```
 alembic revision --autogenerate -m “First”
 alembic upgrade head
```

4. Запуск сервера:

```
uvicorn main:app --reload 
```
