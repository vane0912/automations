from flask import Flask
from automations import homepage, weekly, applications

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(homepage.bp)
    app.register_blueprint(weekly.bp)
    app.register_blueprint(applications.bp)

    
    return app
