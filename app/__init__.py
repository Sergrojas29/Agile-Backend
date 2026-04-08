from flask import Flask



from flask_cors import CORS
from config import config


from app.routes.user import user_bp
from app.routes.main import main
from app.routes.project import project_bp
from app.routes.sprint import sprint_bp
from app.routes.task import task_bp


def create_app(config_name = 'default'):
    app = Flask(__name__)
    CORS(app)
    
    # REGISTER BLUEPRINTS 
    app.register_blueprint(user_bp)
    app.register_blueprint(main)
    app.register_blueprint(project_bp)
    app.register_blueprint(sprint_bp)
    app.register_blueprint(task_bp)
    
    app.config.from_object(config[config_name])

    
    
    return app