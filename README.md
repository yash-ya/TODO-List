# Todo List App

This is a simple Todo List API built with Django.

## Installation

1. Clone the repository: git clone <https://github.com/yash-ya/TODO-List.git>
2. Install dependencies: pip install -r requirements.txt
3. Apply database migrations: python manage.py migrate
4. Run the development server: python manage.py runserver

## Endpoints

## TODO-List API

This API provides endpoints to manage tasks.

### Endpoints:

1. **List and Create Tasks**

   - **URL**: `/tasks/`
   - **Method**: `GET` (List), `POST` (Create)
   - **Description**:
     - `GET`: Retrieves a list of all tasks.
     - `POST`: Creates a new task.
   - **Response Format**: JSON
   - **Authentication**: Not required

2. **Retrieve, Update, and Delete Task by ID**

   - **URL**: `/tasks/<int:pk>/`
   - **Method**: `GET` (Retrieve), `PUT` (Update), `DELETE` (Delete)
   - **Description**:
     - `GET`: Retrieves details of a specific task identified by its ID.
     - `PUT`: Updates details of a specific task identified by its ID.
     - `DELETE`: Deletes a specific task identified by its ID.
   - **Response Format**: JSON
   - **Authentication**: Not required

3. **Get All Tasks (Custom Endpoint)**

   - **URL**: `/get_all/`
   - **Method**: `GET`
   - **Description**: Retrieves all tasks.
   - **Response Format**: JSON
   - **Authentication**: Not required

4. **Add Task (Custom Endpoint)**

   - **URL**: `/add/`
   - **Method**: `POST`
   - **Description**: Adds a new task.
   - **Request Body Format**: JSON
   - **Response Format**: JSON
   - **Authentication**: Not required

5. **Get Task by ID (Custom Endpoint)**

   - **URL**: `/get/<int:id>/`
   - **Method**: `GET`
   - **Description**: Retrieves details of a specific task identified by its ID.
   - **Response Format**: JSON
   - **Authentication**: Not required

6. **Update Task by ID (Custom Endpoint)**

   - **URL**: `/update/<int:id>/`
   - **Method**: `PUT`
   - **Description**: Updates details of a specific task identified by its ID.
   - **Request Body Format**: JSON
   - **Response Format**: JSON
   - **Authentication**: Not required

7. **Delete Task by ID (Custom Endpoint)**
   - **URL**: `/delete/<int:id>/`
   - **Method**: `DELETE`
   - **Description**: Deletes a specific task identified by its ID.
   - **Response Format**: JSON
   - **Authentication**: Not required

### Authentication:

Authentication is not required to access any of the endpoints.

### Error Handling:

The API returns appropriate error responses with status codes and error messages in case of invalid requests or server errors.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please submit a pull request or open an issue.
