from flask import request, jsonify, Blueprint
from app.models.sprint import Sprint 
from app.database import SessionLocal

# ============================================================
# Sprint routes
# ============================================================
sprint_bp = Blueprint('sprint',__name__)

#Get sprints
@sprint_bp.route("/sprints",methods=["GET"])
def get_sprints():
    db = SessionLocal()

    try: 
        sprints = db.query(Sprint).all()

        result = [sprint.to_dict() for sprint in sprints]

        return jsonify(result)
    
    finally:
        db.close()

#get a sprint 
@sprint_bp.route("/sprints/<uuid:sprint_id>", methods=["GET"])
def get_sprint(sprint_id):
    db = SessionLocal() 
    try: 
        sprint = db.query(Sprint).get(sprint_id)
        
        if not sprint: 
            return jsonify({"message":"sprint is not found"}),404

        result = sprint.to_dict()

        return jsonify(result)
    finally: 
        db.close()

#post a sprint 
@sprint_bp.route("/sprints",methods=["POST"])
def post_sprint():
    db = SessionLocal()
    # this on has two system produced variables, end at is the only two 
    # that uses our input 
    try: 
        data = request.json

        sprint = Sprint(
            title = data["title"],
            end_at = data["end_at"],
            project_id = data["project_id"]
        )
        db.add(sprint)
        db.commit
        db.refresh(sprint)
    finally: 
        db.close()

#update a sprint
@sprint_bp.route("/sprints/<uuid:sprint_int>", methods=["PUT"])
def update_sprint(sprint_id): 
    db = SessionLocal()
    try: 
        data = request.json
        sprint = db.query(Sprint).get(sprint_id)

        sprint.title = data.get("title", sprint.title)
        sprint.end_at = data.get("end_at", sprint.end_at)

        db.commit()
        db.refresh(sprint)

        return(jsonify(sprint.to_dict()),200)

    finally:
        db.close()

#delete a sprint 
@sprint_bp.route("/sprints/<uuid:sprint_id>",methods=["DELETE"])
def delete_sprint(sprint_id): 
    db = SessionLocal()

    try: 
        sprint = db.query(Sprint).get(sprint_id)
        if not sprint: 
            return jsonify({"error": "the sprint does not exist"}),404

        db.delete(sprint)
        db.commit()

        return jsonify({"message":"sprint has been deleted"}),200 

    finally: 
        db.close()

