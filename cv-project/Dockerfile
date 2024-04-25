FROM python:3.9.13-slim-buster


WORKDIR /cv-project
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


COPY . .

EXPOSE 5000


CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]