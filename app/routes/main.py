from flask import Blueprint, jsonify
from tests.utils import FilloutDataBase
from init_db import teardown_database, setup_database

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "<h1>Hello from Render!</h1><p>Status: Online</p>"




@main.route('/api/db_create')
def api_db_create():
    setup_database()
    FilloutDataBase.createTestDataBase()
    
    return "Data Base Created"

@main.route('/api/db_drop')
def api_db_drop():
    
    teardown_database()
    
    return "Data Base removed"