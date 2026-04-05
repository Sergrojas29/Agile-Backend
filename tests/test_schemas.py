import unittest
from marshmallow import ValidationError
from app.schemas.project_schema import ProjectSchema, ProjectUpdateSchema
from app.schemas.user_schema import UserSchema, UserUpdateSchema
from app.schemas.task_schema import TaskSchema, TaskUpdateSchema
from app.schemas.sprint_schema import SprintSchema, SprintUpdateSchema

class TestProjectSchema(unittest.TestCase):

    def test_valid_project(self):
        data = {
            "title": "Test Project",
            "end_at": "2026-12-31",
            "owner_id": "00000000-0000-0000-0000-000000000001"
        }
        result = ProjectSchema().load(data)
        self.assertEqual(result["title"], "Test Project")

    def test_missing_title(self):
        data = {
            "end_at": "2026-12-31",
            "owner_id": "00000000-0000-0000-0000-000000000001"
        }
        with self.assertRaises(ValidationError) as ctx:
            ProjectSchema().load(data)
        self.assertIn("title", ctx.exception.messages)

    def test_missing_end_at(self):
        data = {
            "title": "Test Project",
            "owner_id": "00000000-0000-0000-0000-000000000001"
        }
        with self.assertRaises(ValidationError) as ctx:
            ProjectSchema().load(data)
        self.assertIn("end_at", ctx.exception.messages)

    def test_title_too_long(self):
        data = {
            "title": "x" * 51,
            "end_at": "2026-12-31",
            "owner_id": "00000000-0000-0000-0000-000000000001"
        }
        with self.assertRaises(ValidationError) as ctx:
            ProjectSchema().load(data)
        self.assertIn("title", ctx.exception.messages)

    def test_update_all_optional(self):
        result = ProjectUpdateSchema().load({})
        self.assertEqual(result, {})


class TestUserSchema(unittest.TestCase):

    def test_valid_user(self):
        data = {
            "name": "Sergio",
            "username": "sergio123",
            "email": "sergio@gmail.com",
            "password": "securepassword"
        }
        result = UserSchema().load(data)
        self.assertEqual(result["username"], "sergio123")

    def test_missing_email(self):
        data = {
            "name": "Sergio",
            "username": "sergio123",
            "password": "securepassword"
        }
        with self.assertRaises(ValidationError) as ctx:
            UserSchema().load(data)
        self.assertIn("email", ctx.exception.messages)

    def test_invalid_email(self):
        data = {
            "name": "Sergio",
            "username": "sergio123",
            "email": "notanemail",
            "password": "securepassword"
        }
        with self.assertRaises(ValidationError) as ctx:
            UserSchema().load(data)
        self.assertIn("email", ctx.exception.messages)

    def test_password_too_short(self):
        data = {
            "name": "Sergio",
            "username": "sergio123",
            "email": "sergio@gmail.com",
            "password": "short"
        }
        with self.assertRaises(ValidationError) as ctx:
            UserSchema().load(data)
        self.assertIn("password", ctx.exception.messages)

    def test_update_all_optional(self):
        result = UserUpdateSchema().load({})
        self.assertEqual(result, {})


class TestTaskSchema(unittest.TestCase):

    def test_valid_task(self):
        data = {
            "title": "Test Task",
            "due_at": "2026-12-31",
            "value": 5,
            "user_id": "00000000-0000-0000-0000-000000000001",
            "sprint_id": "00000000-0000-0000-0000-000000000002"
        }
        result = TaskSchema().load(data)
        self.assertEqual(result["title"], "Test Task")

    def test_missing_required_fields(self):
        with self.assertRaises(ValidationError) as ctx:
            TaskSchema().load({})
        self.assertIn("title", ctx.exception.messages)
        self.assertIn("due_at", ctx.exception.messages)
        self.assertIn("value", ctx.exception.messages)

    def test_negative_value(self):
        data = {
            "title": "Test Task",
            "due_at": "2026-12-31",
            "value": -1,
            "user_id": "00000000-0000-0000-0000-000000000001",
            "sprint_id": "00000000-0000-0000-0000-000000000002"
        }
        with self.assertRaises(ValidationError) as ctx:
            TaskSchema().load(data)
        self.assertIn("value", ctx.exception.messages)

    def test_update_all_optional(self):
        result = TaskUpdateSchema().load({})
        self.assertEqual(result, {})


class TestSprintSchema(unittest.TestCase):

    def test_valid_sprint(self):
        data = {
            "title": "Sprint 1",
            "end_at": "2026-12-31",
            "project_id": "00000000-0000-0000-0000-000000000001"
        }
        result = SprintSchema().load(data)
        self.assertEqual(result["title"], "Sprint 1")

    def test_missing_required_fields(self):
        with self.assertRaises(ValidationError) as ctx:
            SprintSchema().load({})
        self.assertIn("title", ctx.exception.messages)
        self.assertIn("end_at", ctx.exception.messages)

    def test_update_all_optional(self):
        result = SprintUpdateSchema().load({})
        self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main()