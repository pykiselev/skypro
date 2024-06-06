# Проект "Это моя первая страница на GitHub"

## Описание:

Это моя страница на GitHub с проектами в рамках обучения в SkyPro

## Установка:

1. Клонируйте репозиторий:
```
git clone 
```
https://github.com/pykiselev/skypro.git
2. Установите зависимости:
```
pip install -r requirements.txt
```

3. Создайте базу данных и выполните миграции:
```
python manage.py migrate
```

4. Запустите локальный сервер:
```
python manage.py runserver
```
## Использование:

1. Перейдите на страницу в вашем веб-браузере.
2. Создайте новую учетную запись или войдите существующей.
3. Создайте новую запись в блоге или оставьте комментарий к существующей.

## Документация:

Дополнительную информацию о структуре проекта и API можно найти в [документации](docs/README.md).

## Функции

Функция принимает на вход номер карты и возвращает ее маску
Функция принимает на вход номер счета и возвращает его маску

Функция маскировки номера карты/счета
Функция форматирования даты

Функция сортировки по дате
Функция фильтрации по state

Генератор фильтра по заданной валюте
Функция-генератор описания каждой операции
Генератор номеров банковских карт

## Тестирование

В проект добавлены тесты по всем функциям в src

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).