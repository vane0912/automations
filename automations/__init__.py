from flask import Flask, current_app
from dotenv import load_dotenv
import os
import chromedriver_binary

load_dotenv()
 
class Config(): 
    ENVIROMENT_VARIABLE = os.getenv('RAILWAY_ENVIRONMENT')
    URL_VARIABLE = os.getenv('RAILWAY_STATIC_URL')

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    from .homepage import homepage_bp
    from .weekly import weekly_bp
    from .applications import applications_bp
    
    app.register_blueprint(homepage_bp)
    app.register_blueprint(weekly_bp)
    app.register_blueprint(applications_bp)

    return app
