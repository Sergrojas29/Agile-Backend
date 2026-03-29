import unittest
from dataclasses import dataclass
from init_db import setup_database, teardown_database
from sqlalchemy.exc import IntegrityError
from app import create_app
import json

from datetime import date





from app.database import SessionLocal
from app.models.user import User
from app import create_app
  
#!  python -m unittest discover
class TestRouterProject(unittest.TestCase):
    
    def setUp(self) -> None:
        setup_database()
        self.app = create_app('testing')
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()
        self.db = SessionLocal() 


    def tearDown(self) -> None:
        teardown_database()
        self.db.close()
        
    # GET /projects
    def test_get_projects_returns_200(self):
        response = self.client.get("/projects")
        self.assertEqual(response.status_code, 200)
    
    # GET /projects/<id>
    def test_get_project_not_found(self):
        response = self.client.get("/projects/00000000-0000-0000-0000-000000000000")
        self.assertEqual(response.status_code, 404)
    
    # GET /project/<id>
    def test_get_one_project(self):
        #create db and get project id
        self.client.get("/api/db_create")
        project_data = self.client.get("/projects")
        project_id = project_data.get_json()[0]["id"]
        
        
        response = self.client.get(f"/projects/{project_id}")
        self.assertEqual(response.status_code, 200)
      
        
    # POST /projects
    def test_post_project_success(self):
        
        #Create and get one user id
        self.client.get("/api/db_create")
        user_data = self.client.get("/users")
        user_id = user_data.get_json()[0]["id"]    
        
        
        response = self.client.post("/projects",
            data=json.dumps({
                "title": "Test Project",
                "description": "A good description",
                "end_at": "2025-12-31",
                "owner_id": f"{user_id}"
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

    def test_post_project_missing_fields(self):
        response = self.client.post("/projects",
            data=json.dumps({"description": "missing name and end_at"}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)

    # PUT /projects/<id>
    def test_update_project_not_found(self):
        response = self.client.put("/projects/00000000-0000-0000-0000-000000000000",
            data=json.dumps({"title": "Updated"}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 404)
        
    # PUT /projects/<id>
    def test_update_one_project(self):
        
        #create db and get project id
        self.client.get("/api/db_create")
        project_data = self.client.get("/projects")
        project_id = project_data.get_json()[0]["id"] 
        
        
        
        response = self.client.put(f"/projects/{project_id}",
            data=json.dumps({"title": "Updated"}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)

    # DELETE /projects/<id>
    def test_delete_project_not_found(self):
        response = self.client.delete("/projects/00000000-0000-0000-0000-000000000000")
        self.assertEqual(response.status_code, 404)

    # DELETE /projects/<id>
    def test_delete_one_project(self):
        
        #create db and get project id
        self.client.get("/api/db_create")
        project_data = self.client.get("/projects")
        project_id = project_data.get_json()[0]["id"] 
        
        #test project count
        project_count = len(project_data.get_json())
        
        response = self.client.delete(f"/projects/{project_id}")
        self.assertEqual(response.status_code, 200)
        
        project_data = self.client.get("/projects")
        new_project_count = len(project_data.get_json())
        
        self.assertEqual(project_count-1, new_project_count)


if __name__ == "__main__":
    unittest.main()