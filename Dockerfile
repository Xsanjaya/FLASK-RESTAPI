
FROM python:3.9-alpine

COPY ./requirements.txt /app/requirements.txt
COPY ./.env.example /app/.env

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["./app.py" ]
