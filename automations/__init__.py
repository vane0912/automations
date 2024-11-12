from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .homepage import homepage_bp
    from .weekly import admin
    from .applications import applications_bp
    
    app.register_blueprint(homepage_bp)
    app.register_blueprint(admin)
    app.register_blueprint(applications_bp)

    return app
