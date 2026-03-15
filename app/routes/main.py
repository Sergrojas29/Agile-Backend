from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "<h1>Hello from Render!</h1><p>Status: Online</p>"

@main.route('/api/test')
def api_test():
    # Simple JSON test
    return jsonify({
        "message": "Connection successful",
        "status": 200,
        "tech_stack": "Python Flask"
    })