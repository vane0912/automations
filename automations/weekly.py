from flask import render_template
from flask import Blueprint

weekly_bp = Blueprint('weekly', __name__)

@weekly_bp.route('/weekly')
def weekly():
    return render_template('weekly.html')