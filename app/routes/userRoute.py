from flask import Flask, request, jsonify, Blueprint


from app.models.user import User
from app.database import SessionLocal





user_bp = Blueprint('user', __name__)

# @user_bp.route('/', methods=['POST'])
# def create_user():



#GET users 
@user_bp.route("/users", methods=["GET"])
def get_users(): 
    # users = User()

    return "temp"
