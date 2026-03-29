import unittest
import json
from app import create_app
from app.database import SessionLocal
from app.models.project import Project

# class TestProjectRoutes(unittest.TestCase):
#     pass

#     def setUp(self):
#         self.app = create_app('testing')
#         self.app.config["TESTING"] = True
#         self.client = self.app.test_client()
#         self.db = SessionLocal()  # add this

#     def tearDown(self):
#         self.db.close()

#     # GET /projects
#     def test_get_projects_returns_200(self):
#         response = self.client.get("/projects")
#         self.assertEqual(response.status_code, 200)

#     # GET /projects/<id>
#     def test_get_project_not_found(self):
#         response = self.client.get("/projects/00000000-0000-0000-0000-000000000000")
#         self.assertEqual(response.status_code, 404)

#     # POST /projects
#     def test_post_project_success(self):
#         response = self.client.post("/projects",
#             data=json.dumps({
#                 "name": "Test Project",
#                 "end_at": "2025-12-31"
#             }),
#             content_type="application/json"
#         )
#         self.assertEqual(response.status_code, 201)

#     def test_post_project_missing_fields(self):
#         response = self.client.post("/projects",
#             data=json.dumps({"description": "missing name and end_at"}),
#             content_type="application/json"
#         )
#         self.assertEqual(response.status_code, 400)

#     # PUT /projects/<id>
#     def test_update_project_not_found(self):
#         response = self.client.put("/projects/00000000-0000-0000-0000-000000000000",
#             data=json.dumps({"name": "Updated"}),
#             content_type="application/json"
#         )
#         self.assertEqual(response.status_code, 404)

#     # DELETE /projects/<id>
#     def test_delete_project_not_found(self):
#         response = self.client.delete("/projects/00000000-0000-0000-0000-000000000000")
#         self.assertEqual(response.status_code, 404)


# if __name__ == "__main__":
#     unittest.main()
