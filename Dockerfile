# pull the official base image
FROM python:3.12.0

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG SECRET_KEY
ARG DSN
# Les deux variavles SECRET_KEY et DSN sont à renseigner en cas de construction en local(développement) avec cette commande : 
# docker build -t lettings --build-arg SECRET_KEY="django_key" --build-arg DSN="dsn_key" .
ENV SECRET_KEY=${SECRET_KEY}
ENV DSN=${DSN}

ENV PORT 8000

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt


# copy project 
COPY . /usr/src/app

# Permet de prendre les fichier statics et les déposer dans static files
RUN python manage.py collectstatic --noinput

# Exposez le port sur lequel l'application Django s'exécute
EXPOSE 8000


CMD gunicorn --bind 0.0.0.0:$PORT oc_lettings_site.wsgi