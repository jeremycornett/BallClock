# Use an official Python runtime as a base image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the needed contents into the container at /app
COPY ballclock/dist/theclock-1.0.0.tar.gz /app/
COPY ballclock/run.py /app/

# Install any needed packages specified in requirements.txt
RUN pip install theclock-1.0.0.tar.gz
