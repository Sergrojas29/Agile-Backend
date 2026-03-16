from flask import request, jsonify, Blueprint
from app.models.project import Project
from app.database import SessionLocal

# ============================================================
# Project routes
# ============================================================
project_bp = Blueprint('projects', __name__)

#Getting all projects
@project_bp.route("/projects",methods=["GET"])
def get_projects():
    db = SessionLocal()
    try: 
        projects = db.query(Project).all()
        result = [project.to_dict() for project in projects]

        return jsonify(result)
    finally: 
        db.close()

#Getting a project
@project_bp.route("/projects/<uuid:project_id>", methods=["GET"])
def get_project(project_id): 
    db = SessionLocal()
    try: 
        project = db.query(Project).get(project_id)
        if not project: 
            return jsonify({"error": "project is not found "}),404

        result = project.to_dict()

        return jsonify(result)
    finally:
        db.close()

# Making a project
@project_bp.route("/projects",methods=["POST"])
def post_project(): 
    db = SessionLocal()
    try: 
        data = request.json 
        project = Project(
           name = data["name"],
           description = data.get("description"),
           end_at = data["end_at"] 
        )

        db.add(project)
        db.commit()
        db.refresh(project)

        return(jsonify(project.to_dict()),201)
    
    finally: 
        db.close()

# Updating a project 
@project_bp.route("/projects/<uuid:project_id>",methods=["PUT"])
def update_project(project_id): 
    db = SessionLocal() 
    try: 
        data = request.json 
        project = db.query(Project).get(project_id)

        if not project: 
            return jsonify({"error": "the project is not found"}),404

        project.name = data.get("name", project.name)
        project.description = data.get("description", project.description)
        project.end_at = data.get("end_at", project.end_at)

        db.commit()
        db.refresh(project)

        return jsonify(project.to_dict()),200
    finally: 
        db.close()

# Deleting 
@project_bp.route("/projects/<uuid:project_id>",methods=["DELETE"])
def delete_project(project_id): 
    db = SessionLocal()

    try: 
        project = db.query(Project).get(project_id)
        if not project: 
            return jsonify ({"error": "the project is not found"}),404

        db.delete(project)
        db.commit()

        return jsonify({"message":"the project has been deleted"}),200
    finally: 
        db.close()
