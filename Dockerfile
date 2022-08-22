
FROM python:3.9-alpine

COPY requirements.txt /app/requirements.txt
COPY .env.example /app/.env
COPY app/. /app

WORKDIR /app

RUN pip install -r requirements.txt
RUN flask db init
RUN flask db migrate
RUN flask db upgrade

ENTRYPOINT [ "python3" ]

CMD ["app.py" ]
