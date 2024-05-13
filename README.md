# File Parsing Service

This is a simple web application built with Flask, designed to process various file formats such as CSV, JSON, and TXT. The application utilizes Prometheus for monitoring and metrics collection.

## Technologies Used

- **Python:** Programming language used for backend development.
- **Flask:** Web framework used for building the web application.
- **Prometheus:** Monitoring and metrics collection tool.
- **Docker:** Containerization technology used for deployment.
- **HTML/CSS:** Used for frontend templates and styling

## Description

The application provides an interface to upload files, which are then processed based on their format. Uploaded files are saved to the uploads folder. Currently supported formats include CSV, JSON, and TXT. After processing, a summary of the file content is displayed to the user.

## Usage

To run the application, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Docker installed.
3. Ensure that Docker Desktop is running on your system.
4. Navigate to the project directory.
5. If You run program for the first time build the Docker containers:

```
docker-compose up --build
```

6. Next time run command:

```
docker-compose up
```

7. Access the application in your web browser at http://localhost:5000.

8. Upload a file using the provided interface and view the processed summary.

## Prometheus Monitoring

Prometheus is configured to collect metrics from the application. Metrics can be accessed by navigating to http://localhost:9090 and also http://localhost:5000/metrics.

## Directory Structure

- **app.py:** Main Flask application file.
- **process_file_format.py:** Module for processing different file formats.
- **templates:** HTML templates for the frontend.
- **static:** Static assets such as CSS files.
- **Dockerfile:** Docker configuration for building the application image.
- **requirements.txt:** Python dependencies

## Docker Configuration

The application is containerized using Docker for easy deployment and portability. Docker Compose is used to manage the application and Prometheus containers.
