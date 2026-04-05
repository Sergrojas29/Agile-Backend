# Schema Validation Documentation
 
This project uses [Marshmallow](https://marshmallow.readthedocs.io/) for request body validation. All incoming JSON data is validated before being processed or saved to the database.
 
---
 
## Project Schema
 
### ProjectSchema (POST)
 
Used when creating a new project.
 
| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| title | String | yes | max 50 characters |
| description | String | no | max 500 characters |
| start_at | Date | no | format YYYY-MM-DD |
| end_at | Date | yes | format YYYY-MM-DD |
| owner_id | UUID | yes | must be a valid UUID |
 
### ProjectUpdateSchema (PUT)
 
Used when updating an existing project. All fields are optional.
 
| Field | Type | Constraints |
|-------|------|-------------|
| title | String | max 50 characters |
| description | String | max 500 characters |
| start_at | Date | format YYYY-MM-DD |
| end_at | Date | format YYYY-MM-DD |
| owner_id | UUID | must be a valid UUID |
 
---
 
## User Schema
 
### UserSchema (POST)
 
Used when creating a new user.
 
| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| name | String | yes | max 50 characters |
| username | String | yes | max 50 characters |
| email | String | yes | must be a valid email |
| password | String | yes | min 8, max 255 characters |
| role | String | no | max 50 characters |
| is_admin | Boolean | no | defaults to false |
 
### UserUpdateSchema (PUT)
 
Used when updating an existing user. All fields are optional.
 
| Field | Type | Constraints |
|-------|------|-------------|
| name | String | max 50 characters |
| username | String | max 50 characters |
| email | String | must be a valid email |
| password | String | min 8, max 255 characters |
| role | String | max 50 characters |
| is_admin | Boolean | |
 
---
 
## Task Schema
 
### TaskSchema (POST)
 
Used when creating a new task.
 
| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| title | String | yes | max 50 characters |
| description | String | no | max 500 characters |
| start_at | Date | no | format YYYY-MM-DD |
| due_at | Date | yes | format YYYY-MM-DD |
| value | Integer | yes | must be 0 or greater |
| user_id | UUID | yes | must be a valid UUID |
| sprint_id | UUID | yes | must be a valid UUID |
 
### TaskUpdateSchema (PUT)
 
Used when updating an existing task. All fields are optional.
 
| Field | Type | Constraints |
|-------|------|-------------|
| title | String | max 50 characters |
| description | String | max 500 characters |
| start_at | Date | format YYYY-MM-DD |
| due_at | Date | format YYYY-MM-DD |
| value | Integer | must be 0 or greater |
| user_id | UUID | must be a valid UUID |
| sprint_id | UUID | must be a valid UUID |
 
---
 
## Sprint Schema
 
### SprintSchema (POST)
 
Used when creating a new sprint.
 
| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| title | String | yes | max 100 characters |
| start_at | Date | no | format YYYY-MM-DD |
| end_at | Date | yes | format YYYY-MM-DD |
| project_id | UUID | yes | must be a valid UUID |
 
### SprintUpdateSchema (PUT)
 
Used when updating an existing sprint. All fields are optional.
 
| Field | Type | Constraints |
|-------|------|-------------|
| title | String | max 100 characters |
| start_at | Date | format YYYY-MM-DD |
| end_at | Date | format YYYY-MM-DD |
| project_id | UUID | must be a valid UUID |
 
---
 
## Error Responses
 
If validation fails, the API returns a 400 status code with a JSON body describing the errors.
 
example request:
```json
{
  "description": "missing required fields"
}
```
 
example response:
```json
{
  "errors": {
    "title": ["Missing data for required field."],
    "end_at": ["Missing data for required field."]
  }
}
```
