FROM python:3.7
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r /app/requirements.txt

COPY main.py main.py

EXPOSE 5000

ENTRYPOINT ["/app/main.py"]
