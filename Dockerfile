FROM python:3.5-alpine
MAINTAINER Clifton Barnes <clifton.a.barnes@gmail.com>

ENV FLASK_APP=/app/gui/monitor.py
EXPOSE 80

# Install uwsgi
RUN apk add --no-cache python3-dev build-base linux-headers pcre-dev nodejs && \
    pip install uwsgi==2.0.16 && \
    apk del --purge build-base

COPY . /app

WORKDIR /app/gui/static

RUN npm install && npm run build

WORKDIR /app

RUN pip install pipenv && pipenv install --system

CMD ["uwsgi", "--ini", "/app/uwsgi.ini"]
