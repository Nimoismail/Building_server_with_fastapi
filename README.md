# Building_server_with_fastapi

# FastAPI API with SQLAlchemy

This project is a RESTful API built using the FastAPI framework and SQLAlchemy ORM. It provides endpoints for managing items. the endpoint are the Create, Read, Update, Delete operations

# Features

-The features are of the following
-GET endpoint: Get all items
-GET endpoint: Get a single item by ID
-POST endpoint: Add a new item
-PUT endpoint: Full update of an item
-PATCH endpoint: Partial update of an item
-DELETE endpoint: Delete an item

# inatallation

## Clone the repository:

git@github.com:Nimoismail/Building_server_with_fastapi.git

## Initialize a virtual environment using Pipenv:

        pipenv shell

## Install the required dependencies:

        pipenv install fastapi sqlalchemy uvicorn

## How to start the Start server:

        uvicorn main:app --reload

## Testing the API

The API server will be running locally at http://localhost:8000.

# Endpoints

## GET /get_all_endpoint/

Get all items.

# GET /get_one_endpoint/{id}

Get a single item by ID.

# POST /post_endpoint/

Add a new item. Send a JSON payload with the following fields:

# id (int): Item ID

# name (str): Item Name

--name (string): Item name

# description (str): Item description

--description (string): Item description

# PATCH /patch_endpoint/{id}

Update an item. Send a JSON payload with the following fields:
Update an item with a partial update.
Provide the ID of the item to update and send a JSON payload with the fields to update:

## name

name (string, optional): Updated item name

## description

description (string, optional): Updated item description

# DELETE /delete_endpoint/{id}

Delete an item by ID.

# Technologies Used

--FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.
--SQLAlchemy: An Object-Relational Mapping (ORM) library for Python.
--SQLite: A lightweight and serverless database engine used for local development.
--Uvicorn: A lightning-fast ASGI server used to run the API.



# contributing

contribution are highly welcomed, always fun to contribute

# How to Deploy

Make sure to deploy by merging code to master. It will automatically handle everything for you because we are awesome and all our github action pipelines are up to date.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

# Author

Nimo ismail.