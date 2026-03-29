## Project Milestone 5: SQL Design
**Project:** Agile Backend  
**Purpose:** Database design and testing specification for developers   
**Deployed Test** GitHub BACKEND link : [UNIT TESTING ORM CODE](https://github.com/Sergrojas29/Agile-Backend/tree/python/tests)

---

## Overview

This document describes the **database schema**, **table relationships**, and **data access methods** for the Agile Backend application. It is intended as a **developer-facing design document** that clearly defines how data is stored, accessed, and validated.

This document answers the following questions:
- What tables exist in the database?
- What fields and constraints do those tables contain?
- How are tables related?
- What data access methods are required?
- Which pages depend on which data?
- How do we test both the schema and the access routines?

The backend uses **PostgreSQL** accessed through **SQLAlchemy 2.0** via a Flask web framework and Gunicorn WSGI server.

---

# Database Tables

At minimum, the system requires the following core tables:
- `users`
- `projects`
- `sprints`
- `tasks`


---

## 1) Table: users

### Table Description
Stores user account profiles, roles, and authentication data for the Agile tracking system.

### Fields
| Field Name | Description | Constraints |
|----------|------------|-------------|
| id | Unique user identifier | UUID, Primary key, default uuid4 |
| name | User's full name | String, NOT NULL |
| role | User's job role/title | String, Nullable |
| is_admin | Admin privileges flag | Boolean, default False |
| username | Unique login name | String, Unique, NOT NULL |
| email | User email address | String, Unique, NOT NULL |
| password | Hashed password string | String, NOT NULL |
| created_at | Account creation timestamp | DateTime, NOT NULL, default NOW() |

### Relationships
- One-to-many with `projects` (as `assigned_projects` via `owner_id`)
- One-to-many with `tasks` (as `assigned_tasks`)

### Table Tests

**Use Case Name:** Create user record  
**Description:** Verify a new user can be stored and constraints are enforced.  
**Pre-conditions:** Database running, active `SessionLocal`  
**Test Steps:**
1. Insert valid user row (`session.add(user)`)
2. Commit and query by `username`  
3. Insert invalid user row (Missing `email` field)
**Expected Result:** Valid user persists with generated UUID. Invalid user triggers `IntegrityError` (NotNullViolation).  
**Actual Result:** Database enforces `nullable=False` and accurately returns data.  
**Status:** Pass  

---

## 2) Table: projects

### Table Description
Represents a high-level Agile project that contains multiple sprints.

### Fields
| Field Name | Description | Constraints |
|----------|------------|-------------|
| id | Unique project identifier | UUID, Primary key, default uuid4 |
| title | Project display name | String(50), NOT NULL |
| description | Detailed project scope | String(500), Nullable |
| start_at | Target start date | Date, NOT NULL, server_default current_date |
| end_at | Target end date | Date, NOT NULL |
| owner_id | User who owns the project | Foreign key → users.id, Nullable |

### Relationships
- Many-to-one with `users` (Owner)
- One-to-many with `sprints` (as `assigned_sprints`)

### Table Tests

**Use Case Name:** Create multiple projects  
**Description:** Verify bulk project creation and Identity Map expiration.  
**Pre-conditions:** Owner user exists in the database.  
**Test Steps:**
1. Fetch existing user for `owner_id`.
2. Insert list of projects using `session.add_all()`.  
3. Call `session.flush()` and `session.expire_all()`.
4. Query all projects.
**Expected Result:** Projects are persisted, UUIDs generated, and exact count matches input.  
**Status:** Pass  

---

## 3) Table: sprints

### Table Description
Represents a time-boxed iteration (Sprint) assigned to a specific Project.

### Fields
| Field Name | Description | Constraints |
|----------|------------|-------------|
| id | Unique sprint identifier | UUID, Primary key, default uuid4 |
| title | Sprint iteration name | String(100), NOT NULL |
| start_at | Sprint start date | Date, NOT NULL, server_default current_date |
| end_at | Sprint end date | Date, NOT NULL |
| project_id | Project owning this sprint | Foreign key → projects.id, NOT NULL |

### Relationships
- Many-to-one with `projects`
- One-to-many with `tasks`

### Table Tests

**Use Case Name:** Create sprint  
**Description:** Verify sprint is strictly tied to a project constraint.  
**Test Steps:**
1. Insert sprint with valid `project_id`.  
**Expected Result:** Sprint row created and associated with Project's `assigned_sprints` list.  
**Status:** Pass  

---

## 4) Table: tasks

### Table Description
Tracks individual Agile tasks/tickets within sprints or backlogs.

### Fields
| Field Name | Description | Constraints |
|----------|------------|-------------|
| id | Task identifier | UUID, Primary key, default uuid4 |
| title | Task name | String, NOT NULL |
| description | Detailed task instructions | String, NOT NULL |
| start_at | Expected work start date | Date, NOT NULL |
| due_at | Deadline date | Date, NOT NULL |
| value | Story points | Integer, NOT NULL |
| user_id | Assigned user | Foreign key → users.id, Nullable |
| sprint_id | Associated sprint | Foreign key → sprints.id, Nullable |

### Relationships
- Many-to-one with `sprints` (Optional)
- Many-to-one with `users` (Optional)

### Table Tests

**Use Case Name:** Create orphan/backlog task  
**Description:** Verify optional relationships allow tasks to exist without a sprint or assigned user.  
**Test Steps:**
1. Insert task with `user_id=None` and `sprint_id=None`.  
2. Query task from database.  
**Expected Result:** Task persists successfully as a backlog item without throwing foreign key errors.  
**Status:** Pass  

---

# Data Access Methods

Each table has core access methods managed via Flask routes and SQLAlchemy sessions.

## Create Routes : [ROUTES CODE](https://github.com/Sergrojas29/Agile-Backend/tree/python/app/routes)

## Access Method: RESTful GET (All & Single)
**Description:** Fetches all records or a specific record by UUID.  
**Endpoints:**
-   `GET /users`
-   `GET /users/<id>`
-   `GET /projects`
-   `GET /projects/<id>`
-   `GET /sprints`
-   `GET /sprints/<id>`
-   `GET /tasks`
-   `GET /tasks/<id>`   
**Return:** JSON List or JSON Object (Status 200), or Error (Status 404).

## Access Method: RESTful POST (Create)
**Description:** Parses `request.json` payloads, constructs the ORM object, adds to session, commits, and calls `db.refresh()` to fetch system-generated defaults.  
**Endpoints:**
-   `POST /users`
-   `POST /projects`
-   `POST /sprints`
-   `POST /tasks`  
**Return:** JSON representation of created object (Status 201).

## Access Method: RESTful PUT (Update)
**Description:** Fetches an existing entity by UUID. Uses `.get("key", current_value)` to conditionally update fields, defaulting to the original values if no input is provided.  
**Endpoints:**
-   `PUT /users/<id>`
-   `PUT /projects/<id>`
-   `PUT /sprints/<id>`
-   `PUT /tasks/<id>`  
**Return:** JSON representation of updated object (Status 200), or Error (Status 404).

## Access Method: RESTful DELETE
**Description:** Fetches entity by UUID, runs `db.delete()`, and commits the transaction to remove the record.  
**Endpoints:**
-   `DELETE /users/<id>`
-   `DELETE /projects/<id>`
-   `DELETE /sprints/<id>`
-   `DELETE /tasks/<id>`  
**Return:** JSON success message (Status 200), or Error (Status 404).

## Access Method: Database Seeding & Reset
**Description:** Drops, rebuilds, and populates the database using the internal utility scripts.  
**Endpoints:**
-   `GET /api/db_create`
-   `GET /api/db_drop`  
**Return:** String confirmation message.

---

# Page-to-Database Mapping

| API Endpoint Namespace | Tables Accessed | Purpose |
|----|----------------|----------------|
| `/api/` | all tables | Schema reset and data population |
| `/users` | `users` | User management and profiles |
| `/projects` | `projects` | High-level project boards |
| `/sprints` | `sprints` | Iteration tracking |
| `/tasks` | `tasks` | Ticket manipulation (backlog & active) |

---

# Page Data Access Tests

**Use Case Name:** Update a specific Task (`PUT /tasks/<uuid>`)  
**Description:** Verify that PUT endpoints correctly preserve existing fields while updating specified fields.  
**Pre-conditions:** Task exists in the database.  
**Test Steps:**
1. Send `PUT /tasks/<valid_uuid>` with JSON payload `{"value": 8}`.  
2. Observe the returned JSON object.  
**Expected Result:** The `value` field is updated to 8, but the original `title`, `description`, and `due_at` fields remain unchanged. Returns 200 OK.  
**Status:** Pass  

**Use Case Name:** Handle non-existent IDs gracefully (`GET /projects/<uuid>`)  
**Description:** Verify the API properly catches invalid lookups instead of crashing the server.  
**Pre-conditions:** Database is running.  
**Test Steps:**
1. Send `GET /projects/<random_generated_uuid>`.  
**Expected Result:** Application checks `if not project:`, catches the NoneType, and returns `{"error": "project is not found"}` with a 404 HTTP status code.  
**Status:** Pass  

**Use Case Name:** Initialize Database via API (`GET /api/db_create`)  
**Description:** Ensure the testing reset endpoints successfully scaffold tables.  
**Pre-conditions:** Database connection configured.  
**Test Steps:**
1. Send `GET /api/db_create`.
2. Send `GET /users` to verify population.  
**Expected Result:** `/db_create` returns "Data Base Created". The subsequent `GET /users` returns the populated test accounts in JSON format.  
**Status:** Pass  

---

## Notes
- Constraints enforced strictly at PostgreSQL level (`nullable=False`, unique constraints).
- Relational mapping uses SQLAlchemy `Mapped` and `mapped_column` with `| None` for optional fields.
- UUIDs are utilized for all primary keys to prevent ID enumeration.
- All routes wrap database interactions in `try...finally` blocks calling `db.close()` to prevent connection pooling leaks.