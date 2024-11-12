from flask import render_template
from flask import Blueprint,current_app
homepage_bp = Blueprint('homepage', __name__)

@homepage_bp.route('/')
def homepage():
    url = 'http://127.0.0.1:5000'
    return render_template('homepage.html', goto=url)