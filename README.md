# Тестовое задание для SimbirSoft.

## Настройка окружения и запуск теста

У вас должен быть установлен docker-compose и python не ниже 3.10. Команды данные ниже описаны для Linux.

1. Клонировать репозиторий и перейти в директорию с проектом;
2. Создать и активировать виртуальное окружение:

`python -m venv venv`

`source venv/bin/activate`

3. Установить все необходимые зависимости:

`pip install -r requirements.txt`

4. Поднять docker-compose с Selenium Grid: 

`docker-compose up -d`

5. Поднять docker контейнер для отображений allure отчетов:   

`docker run -d -p 5050:5050 -e CHECK_RESULTS_EVERY_SECONDS=3 -e KEEP_HISTORY=1  -v ${PWD}/allure:/app/allure-results  frankescobar/allure-docker-service`

6. Запустить тест:

`pytest -s -v -k test_replenishment_and_debiting_of_account .`

Так же есть возможность добавить тег `--driver=local` для локального запуска.
Для этого предварительно нужно будет положить WebDriver по пути /usr/local/bin/

Cтек: Python + Pytest + Allure + Selenium Grid

