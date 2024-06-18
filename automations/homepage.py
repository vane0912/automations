from flask import render_template
from flask import Blueprint,current_app
homepage_bp = Blueprint('homepage', __name__)

@homepage_bp.route('/')
def homepage():
    
    print(current_app.config['ENVIROMENT_VARIABLE'])
    return render_template('homepage.html')