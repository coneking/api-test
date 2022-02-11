FROM python:3.9.10-alpine3.15

RUN pip install --upgrade pip

RUN adduser -D -u 1001 app
USER 1001
WORKDIR /app
COPY --chown=1001:1001 app /app

RUN pip install --user --no-cache-dir -r requirements.txt 

CMD [ "python", "./app.py" ]
