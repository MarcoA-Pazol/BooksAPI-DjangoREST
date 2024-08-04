# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/BooksApi

# Upgrade pip
RUN pip install --upgrade pip

# Set the working directory in the container
WORKDIR /BooksApi

# Install dependencies
COPY requirements.txt /BooksApi/

# Copy the project files into the working directory
COPY . /BooksApi/

# Expose the port your application will run on
EXPOSE 8000

# Debug: List installed packages
RUN pip list

# Start the Django server
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
