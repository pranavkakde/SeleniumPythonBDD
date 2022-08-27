FROM python:3.10-alpine3.15 as base
WORKDIR /app
COPY ./features ./features
COPY ./behave.ini ./behave.ini
COPY ./requirements.txt ./requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "-m", "behave"]