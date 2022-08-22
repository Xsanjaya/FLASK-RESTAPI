
FROM python:3.9-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN python -m pip install --upgrade
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["app.py" ]
