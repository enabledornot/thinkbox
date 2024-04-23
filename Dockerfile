FROM python:3.9-slim

WORKDIR /thinkbox

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py app.py
COPY database.py database.py
COPY init.sql init.sql
COPY static static
COPY templates templates

CMD [ "gunicorn", "app:app"]