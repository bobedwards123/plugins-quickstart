# Use an official Python runtime as a parent image
FROM python:3.11.4-bookworm

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5003

# Run main.py when the container launches

# CMD ["hypercorn", "app:app", "-b", "0.0.0.0:80"]

CMD ["python", "main.py"]