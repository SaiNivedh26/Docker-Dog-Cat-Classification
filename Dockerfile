# # Use the official Python image as the base image
# FROM python:3.8-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements file and install dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the Flask application code
# COPY . .

# # Copy the pre-trained model file
# COPY cats_and_dogs_classifier.h5 .

# # Expose the port the app runs on
# EXPOSE 5000

# # Set the environment variable for Flask
# ENV FLASK_APP=app.py

# # Run the Flask application
# CMD ["flask", "run", "--host=0.0.0.0"]
# start by pulling the python image
FROM python:3.11

# switch working directory
RUN mkdir /app

WORKDIR /app


# copy every content from the local file to the image
COPY . .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt
# configure the container to run in an executed manner

CMD ["python","app.py" ]