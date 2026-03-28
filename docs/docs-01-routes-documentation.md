# API Routes Documentation

## Overview
This API is built using Flask and provides CRUD operations for:

- Users  
- Projects  
- Sprints  
- Tasks  

It also includes a basic health check route.

**Base URL:** `/`  
**Content-Type:** `application/json`

---

## Main Routes (`main.py`)

```python
from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "<h1>Hello from Render!</h1><p>Status: Online</p>"

@main.route('/api/db_create')
def api_db_create():
    return "Created"
```

### GET `/`
**Description:**  
Health check endpoint to verify the server is running.

**Response:**
```html
<h1>Hello from Render!</h1><p>Status: Online</p>
```

---

### GET `/api/db_create`
**Description:**  
Placeholder endpoint for database initialization or testing.

**Response:**
```
Created
```

---

## Imports Explanation

### `Blueprint`
Used to organize routes into separate modules. Each group of routes (users, projects, etc.) is defined in its own blueprint.

### `jsonify`
Converts Python data (dicts/lists) into JSON responses and sets the correct headers.

### `request`
Used to access incoming request data (such as JSON body).

### `SessionLocal`
Database session used to interact with the database (queries, inserts, updates).

### Models (`User`, `Project`, `Sprint`, `Task`)
Represent database tables and include a `to_dict()` method for serialization.

---

## User Routes

### GET `/users`
Retrieve all users.

### GET `/users/<user_id>`
Retrieve a single user.

- **Params:** `user_id` (UUID)

**Error:**
```json
{ "error": "User not found/in system" }
```

---

### POST `/users`
Create a new user.

**Body:**
```json
{
  "name": "string",
  "username": "string",
  "email": "string",
  "password": "string",
  "role": "string (optional)",
  "is_admin": "boolean (optional)"
}
```

---

### PUT `/users/<user_id>`
Update a user.

---

### DELETE `/users/<user_id>`
Delete a user.

---

## Project Routes

### GET `/projects`
Retrieve all projects.

### GET `/projects/<project_id>`
Retrieve a single project.

---

### POST `/projects`
Create a project.

**Body:**
```json
{
  "name": "string",
  "description": "string (optional)",
  "end_at": "datetime"
}
```

---

### PUT `/projects/<project_id>`
Update a project.

---

### DELETE `/projects/<project_id>`
Delete a project.

---

## Sprint Routes

### GET `/sprints`
Retrieve all sprints.

### GET `/sprints/<sprint_id>`
Retrieve a single sprint.

---

### POST `/sprints`
Create a sprint.

**Body:**
```json
{
  "title": "string",
  "end_at": "datetime"
}
```

---

### PUT `/sprints/<sprint_id>`
Update a sprint.

---

### DELETE `/sprints/<sprint_id>`
Delete a sprint.

---

## Task Routes

### GET `/tasks`
Retrieve all tasks.

### GET `/tasks/<task_id>`
Retrieve a single task.

---

### POST `/tasks`
Create a task.

**Body:**
```json
{
  "title": "string",
  "description": "string (optional)",
  "due_at": "datetime",
  "value": "number"
}
```

---

### PUT `/tasks/<task_id>`
Update a task.

---

### DELETE `/tasks/<task_id>`
Delete a task.

---

## Notes

- All routes return JSON unless otherwise specified  
- UUIDs are used as identifiers  
- Database sessions are created and closed per request  

---

## Future Improvements

- Add authentication 
- Add request validation
- Add documentation
- Standardize error responses?