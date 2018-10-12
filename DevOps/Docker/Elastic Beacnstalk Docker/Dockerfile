# Use an official Python runtime as a parent image
# FROM python:3.6
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /app

# Add requirements.txt before rest of repo for caching
ADD requirements.txt /app/

# Update pip
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
ADD . /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
