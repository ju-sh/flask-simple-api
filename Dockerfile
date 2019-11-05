FROM python:3.7.4-slim-stretch
# or FROM python:3.7-alpine
WORKDIR /app

COPY *.py /app/
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Setting the name of the Flask app
ENV FLASK_APP main.py

# Make the server visible across network
 ENV FLASK_RUN_HOST 0.0.0.0

# Set the port on which Flask runs
ENV FLASK_RUN_PORT=5000

# Enable Flask debug mode
ENV FLASK_DEBUG=1

EXPOSE 5000

# CMD ["flask", "main.py"]
ENTRYPOINT flask run
