FROM python:3.12-slim-bullseye as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./backend/pyproject.toml ./backend/poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.12-slim-bullseye

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./backend/src /code/src

CMD celery -A src.tasks worker --loglevel=info -B