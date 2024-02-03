# Todo List App

This is a simple Todo List API built with Django.

## Installation

1. Clone the repository: git clone <https://github.com/yash-ya/TODO-List.git>
2. Install dependencies: pip install -r requirements.txt
3. Apply database migrations: python manage.py migrate
4. Run the development server: python manage.py runserver

## Endpoints

### Tasks

- **List Tasks**: `GET /api/tasks/`
- Retrieve a list of all tasks.

- **Create Task**: `POST /api/tasks/`
- Create a new task.
- Example Request Body:

```
{
    "title": "Task 1",
    "description": "Description of Task 1"
}
```

- **Retrieve Task**: `GET /api/tasks/<task_id>/`
- Retrieve details of a specific task.

- **Update Task**: `PUT /api/tasks/<task_id>/`
- Update details of a specific task.
- Example Request Body:

```
{
    "title": "Updated Task 1",
    "description": "Updated description of Task 1"
}
```

- **Delete Task**: `DELETE /api/tasks/<task_id>/`
- Delete a specific task.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please submit a pull request or open an issue.
