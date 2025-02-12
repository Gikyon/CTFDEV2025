# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR ./www

# Install dependencies
RUN pip3 install flask

# Copy the application files into the container
COPY ./www .

# Expose port 80
EXPOSE 80
ENV PORT=80

# Set environment variable to make Flask run in production
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run the Flask app
CMD ["python", "app.py"]
