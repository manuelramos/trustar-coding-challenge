FROM python:3.8

ARG GITHUB_ACCESS_TOKEN=

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "app.py" ]