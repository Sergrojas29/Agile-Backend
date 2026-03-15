from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "<h1>Hello from Render!</h1><p>Status: Online</p>"




@main.route('/api/db_create')
def api_db_create():
    
    
    return "Created"