from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
 
class Config(): 
    ENVIROMENT_VARIABLE = os.getenv('RAILWAY_STATIC_URL')

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # Import blueprints here to avoid circular imports
    from .homepage import homepage_bp
    from .weekly import weekly_bp
    from .applications import applications_bp
    
    app.register_blueprint(homepage_bp)
    app.register_blueprint(weekly_bp)
    app.register_blueprint(applications_bp)

    return app
