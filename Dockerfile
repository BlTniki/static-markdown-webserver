# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
RUN mkdir /static-markdown-webserver
WORKDIR /static-markdown-webserver

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY ./app ./app
COPY ./external ./external
COPY ./configs.py .
COPY ./static-markdown-webserver.py .

# Set the environment variables
ENV DEBUG=${DEBUG:-False} \
    SECRET_KEY=${SECRET_KEY:-you-will-never-guess} \
    PATH_TO_VAULT=${PATH_TO_VAULT:-/static-markdown-webserver/app/md_static/} \
    OFFICIAL_EXTENSIONS_TO_USE=${OFFICIAL_EXTENSIONS_TO_USE:-} \
    OFFICIAL_EXTENSIONS_CONFIG=${OFFICIAL_EXTENSIONS_CONFIG:-}

# Install Nginx
RUN apt-get update && apt-get install -y nginx

# Copy the Nginx configuration file into the container
COPY nginx.conf /etc/nginx/nginx.conf

# Remove the default Nginx configuration file
RUN rm /etc/nginx/sites-enabled/default

# Expose port 80 for Nginx
EXPOSE 80

# Set the entry point for the container
ENTRYPOINT service nginx start && gunicorn --bind 0.0.0.0:5000 static-markdown-webserver:app

# Start a bash shell when the container starts
CMD ["/bin/bash"]