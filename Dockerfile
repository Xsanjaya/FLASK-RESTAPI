
FROM python:3.9-alpine

COPY requirements.txt /app/requirements.txt
COPY .env.example /app/.env

WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD ["app.py" ]
