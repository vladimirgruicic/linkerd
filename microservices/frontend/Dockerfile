# Use the official Python image as the base image
FROM python:3.9

# Set the working directory within the container
WORKDIR /app

# Copy the required files into the container
COPY frontend.py /app/

# Install dependency
RUN pip3 install flask requests

# Specify the command to run when the container starts
CMD [ "python3", "frontend.py" ]
