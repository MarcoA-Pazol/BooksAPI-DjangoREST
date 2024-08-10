# Use the official Python image from the Docker Hub
FROM python:3.10
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/BooksApi

# Set working directory in the container
WORKDIR /BooksApi

# Install dependencies
COPY requirements.txt /BooksApi/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project files into the working directory
COPY . /BooksApi/