from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import blueprints here to avoid circular imports
    from .homepage import homepage_bp
    from .weekly import weekly_bp
    from .applications import applications_bp
    
    app.register_blueprint(homepage_bp)
    app.register_blueprint(weekly_bp)
    app.register_blueprint(applications_bp)

    return app
