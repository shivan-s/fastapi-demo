FROM python:3.13-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -U pip-tools pip
COPY requirements.in /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY app /usr/src/app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

EXPOSE 8000
