FROM python:3.10-slim-buster

WORKDIR /app

# installing required dependencies
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

# copying the application code
COPY *.py .

# exposing the application port
EXPOSE 5000

ENV FLASK_APP=app.py

# running the appplication
CMD [ "flask", "run", "--host", "0.0.0.0" ]