FROM python:3.10

WORKDIR /iksvan

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .