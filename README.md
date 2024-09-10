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

### Склонировать сервисы в подмодулях

```bash
git submodule update --init --recursive
```

### Ознакомиться с инструкциями в каждом подмодуле

[products-service](https://github.com/matthew-mar/products-service/tree/3c393abaa6f818fe949cc369ff74cb71a0819793)

[history-service](https://github.com/matthew-mar/history-service/tree/6e22c65b433b988a9b29e256e40302d938635681)

### Запуск приложения

```bash
docker-compose up --build
```

### Применение миграций (одинаково для каждого сервиса)

#### 1. Зайти в контейнер сервиса

```bash
docker exec -it <service_name> /bin/sh
```

#### 2. Применить миграции

```bash
npx prisma migrate dev --name init
```

## Повторный запуск

```bash
docker-compose up
```
