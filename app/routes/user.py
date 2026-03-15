# from models.user import User
from flask import Flask, request, jsonify, Blueprint


user_bp = Blueprint('user', __name__)


#GET users 
@user_bp.route("/users", methods=["GET"])
def get_users(): 
    # users = User()

    return "temp"
