from flask import request, jsonify, Blueprint
from app.models.task import Task 
from app.database import SessionLocal

# ============================================================
# Task routes
# ============================================================
task_bp = Blueprint('task',__name__)

#Getting all the tasks
@task_bp.route("/tasks",methods=["GET"])
def get_tasks():
    db = SessionLocal()
    try:
        tasks = db.query(Task).all()

        result = [task.to_dict() for task in tasks]

        return jsonify(result)
    finally:
        db.close() 

#Getting one task 
@task_bp.route("/tasks/<uuid:task_id>",methods=["GET"])
def get_task(task_id):
    db = SessionLocal()

    try:
        task = db.query(Task).get(task_id)
        if not task:
            return jsonify({"error":"the task is not found"}),404
        result = task.to_dict()

        return jsonify(result)
    
    finally:
        db.close()

#Create a task
@task_bp.route("/tasks",methods=["POST"])
def post_task():
    db = SessionLocal()
    try:
        data = request.json

        task = Task(
            title = data["title"],
            description = data.get("description"),
            due_at = data["due_at"],
            value = data["value"],
            user_id = data["user_id"],
            sprint_id = data["sprint_id"]
        )
        db.add(task)
        db.commit()
        db.refresh(task) # making sure all system inputted values are saved

        return jsonify(task.to_dict()),201
    finally:
        db.close()

#Update one task
@task_bp.route("/tasks/<uuid:task_id>",methods=["PUT"])
def update_task(task_id):
    db = SessionLocal()
    try:
        data = request.json #user input

        task = db.query(Task).get(task_id)
        if not task:
            return jsonify({"error":"no task is found"}),404
        
        #updating the fields, default prev value if no new one
        task.title = data.get("title",task.title)
        task.description = data.get("description",task.description)
        task.due_at = data.get("due_at",task.due_at)
        task.value = data.get("value",task.value)

        db.commit()
        db.refresh(task)

        result = task.to_dict()

        return jsonify(result),200
    
    finally:
        db.close()

#Delete one task  
@task_bp.route("/tasks/<uuid:task_id>", methods=["DELETE"])
def delete_task(task_id):
    db = SessionLocal() 

    try:

        task = db.query(Task).get(task_id) 
        if not task:
            db.close()
            return jsonify({"error": "Task not found"}),404

        db.delete(task)
        db.commit()

        return jsonify({"message":"task has been deleted"}),200
    finally:
        db.close()
