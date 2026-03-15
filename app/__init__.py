from flask import Flask



from config import config



from app.routes.userRoute import user_bp
from app.routes.main import main


def create_app(config_name = 'default'):
    app = Flask(__name__)
    
    
    # REGISTER BLUEPRINTS 
    app.register_blueprint(user_bp)
    app.register_blueprint(main)
    
    app.config.from_object(config[config_name])

    
    
    return app