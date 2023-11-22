FROM python:3.11.6-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN pip install poetry && poetry install

COPY . /app/

CMD ["poetry", "run", "python", "./finbot_django/manage.py", "runserver", "0.0.0.0:8000"]