FROM python:3.9.7


WORKDIR /usr/src/dm_rest
#work dir in container

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r  /usr/src/requirements.txt

COPY . /usr/src/dm_rest

EXPOSE 8000

#CMD [ "python", "manage.py", "migrate"]
#CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]

#Create image Dockerfile - "docker build -t django_flashcards_dockerfile ."
#Start container and name wits port update "docker run --name card -p 8000:8000 -d django_flashcards_dockerfile"