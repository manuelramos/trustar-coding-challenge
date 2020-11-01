FROM python:3.8

ARG GITHUB_ACCESS_TOKEN=

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./poc_app.py" ]