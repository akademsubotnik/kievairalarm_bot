FROM python:3
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

https://stackoverflow.com/questions/56825265/how-to-use-a-python-virtual-environment-copied-to-a-docker-container

https://docs.docker.com/language/python/build-images/

https://pythonspeed.com/articles/activate-virtualenv-dockerfile/

https://www.educative.io/answers/what-is-the-workdir-command-in-docker