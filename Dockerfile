FROM python:3.9

RUN mkdir /courier

WORKDIR /courier

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/courier"

COPY . .


RUN pip install --upgrade pip
RUN pip install -r requirements/requirements.txt

EXPOSE 8001

RUN python manage.py runserver 0.0.0.0:8001 --noreload
