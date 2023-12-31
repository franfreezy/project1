#BASE IMAGE
FROM python:3.12.1

#SET ENV VARIABLES
ENV PYTHONWRITEBYTECODE=1
ENV PYTHONUNBUFFERED =1 

#WE SET WORKDIR
WORKDIR /project1

COPY Pipfile Pipfile.lock /project1/
RUN pip install pipenv
RUN pipenv install --system

COPY .  /project1/