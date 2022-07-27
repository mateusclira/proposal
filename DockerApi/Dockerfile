FROM alpine

RUN apk add --no-cache python3 py3-pip

RUN pip3 install --no-cache-dir fastapi uvicorn

RUN pip3 install --no-cache-dir Flask-command Flask-Cors

EXPOSE 8087

COPY ./app /app

CMD uvicorn app.aplicacao:app --host 0.0.0.0 --port 8087