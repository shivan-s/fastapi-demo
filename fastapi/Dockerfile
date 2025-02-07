FROM python:3.13-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -U pip-tools pip
COPY requirements.in /usr/src/app/
RUN pip-compile requirements.in -o requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py /usr/src/app/

CMD ["fastapi", "run", "main.py"]

EXPOSE 8000
