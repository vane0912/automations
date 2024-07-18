from flask import render_template
from .automations_list import automations_list_weekly
from flask import Blueprint, render_template, request, current_app, jsonify, make_response
from threading import Thread

from flask import Blueprint

weekly_bp = Blueprint('weekly', __name__)

@weekly_bp.route('/weekly')
def weekly():
    
    return render_template('weekly.html', automations_list=automations_list_weekly)