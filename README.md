# Building a Server with FastAPI
This project is a RESTful API built using the FastAPI framework and SQLAlchemy ORM. It provides endpoints for managing items, including Create, Read, Update, and Delete operations.

# Features
The API includes the following features:

GET endpoint: Get all items
GET endpoint: Get a single item by ID
POST endpoint: Add a new item
PUT endpoint: Fully update an item
PATCH endpoint: Partially update an item
DELETE endpoint: Delete an item

# Installation
To get started with the project, follow these steps:

# Clone the repository:


### Copy code

git clone https://github.com/Nimoismail/Building_server_with_fastapi

## Initialize a virtual environment using 
          Pipenv:pipenv shell



# Install the required dependencies:

pipenv install fastapi sqlalchemy uvicorn

### Start the server with:

uvicorn main:app --reload

# Testing the API
The API server will be running locally at http://localhost:8000. You can use tools like cURL or Postman to test the API endpoints.

## Endpoints
The API provides the following endpoints:

GET /get_all_endpoint/: Get all items.
GET /get_one_endpoint/{id}: Get a single item by ID.
POST /post_endpoint/: Add a new item. Send a JSON payload with the following fields:
id (int): Item ID
name (str): Item Name
description (str): Item description
PATCH /patch_endpoint/{id}: Update an item with a partial update. Provide the ID of the item to update and send a JSON payload with the fields to update:
name (string, optional): Updated item name
description (string, optional): Updated item description
DELETE /delete_endpoint/{id}: Delete an item by ID.


# Technologies Used
The following technologies are used in this project:

FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.
SQLAlchemy: An Object-Relational Mapping (ORM) library for Python.
SQLite: A lightweight and serverless database engine used for local development.
Uvicorn: A lightning-fast ASGI server used to run the API.

##  Contributing
Contributions are highly welcomed. We appreciate your input and it's always fun to contribute to this project.

# How to Deploy
To deploy the project, simply merge the code to the master branch. Our GitHub action pipelines are up to date and will handle everything automatically for you.

# License
This project is licensed under the MIT License.

# Author
This project was created by Nimo Ismail.