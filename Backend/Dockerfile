# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . /app/

RUN apt-get update && apt-get -y install cron
WORKDIR /app
COPY ./script/script.py /etc/cron.d/script.py

RUN echo "*/5 * * * * /usr/local/bin/python /etc/cron.d/script.py >> /var/log/cron.log 2>&1" > /etc/cron.d/pythoncron
RUN chmod 0644 /etc/cron.d/pythoncron
RUN crontab /etc/cron.d/pythoncron

RUN touch /var/log/cron.log
