Клонируйте репозиторий проекта с GitHub.
Создайте виртуальное окружение и активируйте его.
Установите зависимости через pip install -r requirements.txt.
Создайте базу данных с названием database_name.
Примените миграции с командами makemigrations и migrate.
Настройте файл .env по образцу .env.sample.
Создайте суперпользователя с помощью команды python manage.py csu.
Запустите сервер разработки командой python manage.py runserver.
Подключите Telegram-бота по ссылке.
Запустите задачи Celery через celery -A config worker --beat --scheduler django --loglevel=info.
Проверьте API-документацию по URL Swagger и Redoc.
