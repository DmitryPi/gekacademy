# Gek Academy    [![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)

Интерактивная платформа по обучению математических наук.

Цель: 



Лицензия: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy study

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Celery

This app comes with Celery.

To run a celery worker:

``` bash
cd study
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [MailHog](https://github.com/mailhog/MailHog) with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

### HTTPS
Сертификаты и ключи хранятся в `certs/*`

Команда для генерации локального сертификата (не подтвержденного)

    $ openssl req -x509 -out localhost.crt -keyout localhost.key -newkey rsa:2048 -nodes -sha256 -subj "/CN=localhost"

Для windows - установить mkcert
    https://words.filippo.io/mkcert-valid-https-certificates-for-localhost/

    $ mkcert -install
    $ mkcert -key-file study.local.key -cert-file study.local.crt localhost 127.0.0.1 ::1 study.local

    hosts file: 127.0.0.1 .study.local

Инструкции по подключению сертификата c docker
    https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html#developing-locally-with-https

## Deployment

Инструкции по деплою

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

Команды

    $ docker-compose -f local.yml up

    $ set(export) COMPOSE_FILE=local.yml  (задать путь к докер конфигу)
    $ docker-compose up
    $ docker-compose up -d  (detached-daemon)

Вызов команды внутри контейнера

    $ docker-compose -f local.yml run --rm django python manage.py migrate
    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser
    $ docker-compose -f local.yml run --rm django pip install

Ребилд

    $ docker-compose -f local.yml up --build

Bash

    $ docker-compose -f local.yml run django bash
        $ exit
