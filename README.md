# crud_copilot_ai

`crud_copilot_ai` is a Flask-based web application designed to perform CRUD (Create, Read, Update, Delete) operations. It leverages SQLAlchemy for database interactions and provides a modular structure for scalability and maintainability. The project includes routes for handling user interactions, templates for rendering HTML pages, and static assets for client-side functionality.

## Features

- **Database Integration**: Uses SQLAlchemy for ORM (Object-Relational Mapping) to interact with the database.
- **Modular Design**: Organized into separate files for routes, models, and configurations.
- **Dynamic Templates**: HTML templates for creating, updating, and displaying data.
- **Validation**: Includes client-side validation using JavaScript.
- **Docker Support**: Comes with a `Dockerfile` and `docker-compose.yml` for containerized deployment.

## Project Structure

- `app.py`: The main entry point for the Flask application.
- `config.py`: Contains configuration variables, such as `SQLALCHEMY_DATABASE_URI` and `SQLALCHEMY_TRACK_MODIFICATIONS`.
- `models.py`: Defines the database models used in the application.
- `routes.py`: Contains the route definitions for handling HTTP requests.
- `templates/`: HTML templates for rendering the UI.
- `static/`: Static files, including JavaScript for client-side validation.
- `test_app.py`: Unit tests for the application.

## Models

The `models.py` file defines the database models for this application. While the exact models are not provided in the workspace details, typical models in a CRUD application might include:

- **User**: Represents a user in the system, with fields like `id`, `name`, `email`, and `password`.
- **Item**: Represents an item or entity being managed, with fields like `id`, `name`, `description`, and `created_at`.

Each model is likely defined as a Python class inheriting from `db.Model` (SQLAlchemy's base class for models). Relationships between models, such as one-to-many or many-to-many, can also be defined using SQLAlchemy's relationship features.

## Requirements

Install the dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```


# Running the Application

## Activate the virtual environment:

```
source venv/bin/activate
```

## Run the Flask application:

```
python app.py
```

## Access the application at http://localhost:5000.

# Testing
Run the unit tests using:

```
source venv/bin/activate
python -m unittest test_app.py
```


# Deployment
Use the provided Dockerfile and docker-compose.yml to deploy the application in a containerized environment.

# To run the application using Docker, follow these steps:
## Build the Docker image:

```
docker build -t crud_copilot .
```

## Run the Docker container:
```
docker run -p 5000:5000 crud_copilot
```

## Access the application: Open your browser and navigate to http://localhost:5000.

# If you are using docker-compose, follow these steps:

## Start the application:

```
docker-compose up --build
```

## Stop the application:

```
docker-compose down
```

## Migrate DB

```
docker exec -it crud_copilot-app-1 flask db migrate -m "Create contact table"
```

## Upgrade Flask DB
```
docker exec -it crud_copilot-app-1 flask db upgrade
```