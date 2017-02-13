# Test  Task

## Setup

### Docker:

Install Docker

    $ https://docs.docker.com/engine/installation/

Install Docker Compose

    $ pip install docker-compose

or

    $ https://docs.docker.com/compose/install/

Build container

    $ docker-compose build django

Create superuser

    $ docker-compose run django python3 manage.py createsuperuser

Run project

    $ docker-compose up django

View project

    $ http://localhost:8000/