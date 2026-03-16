from flask import Flask, request, jsonify, Blueprint
from app.models.user import User
from app.database import SessionLocal

# ============================================================
# User routes
# ============================================================
user_bp = Blueprint('user', __name__)

# getting all the users 
@user_bp.route("/users", methods=["GET"])
def get_users(): 
    db = SessionLocal()

    try:
        users = db.query(User).all() # SELECT * from users table

        result = [user.to_dict() for user in users]

        return jsonify(result)
    
    finally:
        db.close()

#getting a single user 
@user_bp.route("/users/<uuid:user_id>", methods=["GET"])
def get_user(user_id):
    db = SessionLocal()

    try:
        user = db.query(User).get(user_id)

        if not user: 
            #NO USER WITH THAT ID EXISTS - return error 
            return jsonify({"error":"User not found/in system"}),404
        result = user.to_dict()

        return jsonify(result) 
    
    finally:
        db.close()

# Posting a new user 
@user_bp.route("/users", methods=["POST"])
def post_user():
    db = SessionLocal()
    try:
        data = request.json

        user = User(
            name = data["name"],
            role=data.get("role"),
            is_admin=data.get("is_admin"),
            username=data["username"],
            email=data["email"],
            password=data["password"]  
        )
        db.add(user)
        db.commit()
        db.refresh(user) # to prevent errors with the system automated numbers 

        return jsonify(user.to_dict()),201
    finally:
        db.close()

#Editing a user 
@user_bp.route("/users/<uuid:user_id>", methods = ["PUT"])
def update_user(user_id):
    db = SessionLocal()
    try:
        data = request.json

        #get the edited user 
        user = db.query(User).get(user_id)

        if not user: 
            return jsonify({"error":"user is not found"}),404
        
        #Updating the field, if ther is no input then default to current/previous 
        user.role = data.get("role",user.role)
        user.is_admin = data.get("is_admin",user.is_admin)
        user.username = data.get("username",user.username)
        user.email = data.get("email",user.email)
        user.password = data.get("password",user.password) #we will have to pop password for security 

        db.commit()
        db.refresh(user)

        result = user.to_dict()

        return jsonify(result),200
    
    finally:
        db.close()

#Deleting a user
@user_bp.route("/users/<uuid:user_id>", methods=["DELETE"])
def delete_user(user_id):
    db = SessionLocal() 
    try:
    
        user = db.query(User).get(user_id) 
        if not user:
            return jsonify("error":"user is not found"),404

        db.delete(user)
        db.commit()

        return jsonify({"message":"user has been deleted"}),200
    finally:
        db.close()
        