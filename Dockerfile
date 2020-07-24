FROM python:3.6.9-alpine

COPY app /app
WORKDIR /app
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt 

CMD [ "python", "./app.py" ]
