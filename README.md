# alu-AirBnB_clone

AirBnB project- Lana Arafat and Noella Uwayo

Welcome to the AirBnB clone project. This project aims to develop a simplified version of the AirBnB website.



## Project Overview

"AirBnB Clone" is a web application project that leverages Python for the backend and HTML, CSS, and JavaScript for the frontend. It utilizes MySQL databases for efficient data management and to incorporate user authentication. It is built in phases, including API implementation, frontend design, testing, etc.

## Environment

Airbnb clone is designed in the following environment:

- Python Version: 3.4.3
- Editors Used: Github, Vi, Visual Studio Code

## Getting started

To get started, follow these simple steps:

1. Clone this repository:

git clone https://github.com/lanaarafat/alu-AirBnB_clone.git

2. Navigate to the Airbnb directory:

Copy code
cd Airbnb_clone


## Project Structure

- `console.py`: Entry point for the command-line interpreter.
- `models/`: Directory containing data model classes.
- `tests/`: Directory for unit tests.
- `models/engine/`: Directory for storage classes (e.g. file_storage.py).

## Class Models

Here are the core class models used in this project:

- BaseModel: Base class with common attributes (id, created_at, updated_at).
- User: Stores user-related information (email, password, first_name, last_name).
- City: Stores city-specific information (state_id, name).
- State: Stores state-specific information (name).
- Place: Stores detailed property features (city_id, user_id, name, description, etc).
- Review: Stores customer reviews and opinions (place_id, user_id, text).
- Amenity: Stores highlighted amenity information (name).


## Authors

- Mutoni Lana Arafat (GitHub: lanaarafat, Email: a.mutoni1@alusudent.com)
- Noella Uwayo (GitHub: n_Uwayo, Email: n.uwayo@alustudent.com)

Explore, contribute, and enhance the AirBnB_clone project.
