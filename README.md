# em-test-deployer

## Requirements

- python 3.10+
- docker
- docker-compose

## Первый запуск

### Генерация sql для создания схемы БД.

#### 1. Заполнить данные о сервисах в соответствии с db_init.example.ini

```bash
cp db_init.example.ini db_init.ini
```

#### 2. Сгенерировать sql

```bash
python3 db_init.py
```

### Задать параметры БД

```bash
cp db.env.example db.env
```

### Запуск приложения

```bash
docker-compose up --build
```

## Повторный запуск

```bash
docker-compose up
```
