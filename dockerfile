FROM python:3.10

WORKDIR /app

RUN pip install poetry==1.4.2
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY . /app

CMD ["python", "basic_api/app.py"]