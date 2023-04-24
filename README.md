# Тестовое задание для SimbirSoft.

## Настройка окружения и запуск теста

У вас должен быть установлен docker-compose и python. Команды данные ниже описаны для Linux.

1. Клонировать репозиторий и перейти в директорию с проектом;
2. Установить все необходимые зависимости:

`pip install -r requirements.txt`

3. Поднять docker-compose с Selenium Grid: 

`docker-compose up`

4. Поднять docker контейнер для отображений allure отчетов:   

`docker run -d -p 5050:5050 -e CHECK_RESULTS_EVERY_SECONDS=3 -e KEEP_HISTORY=1  -v ${PWD}/allure:/app/allure-results  frankescobar/allure-docker-service`

5. Запустить тест:

`pytest -s -v --driver=local -k test_replenishment_and_debiting_of_account .`

Cтек: Python + Pytest + Allure + Selenium Grid

