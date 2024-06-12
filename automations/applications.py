from .automations_list import automations_list
from flask import Blueprint, render_template, request, jsonify
from itertools import chain

# Define a blueprint for your applications
applications_bp = Blueprint('applications', __name__)

@applications_bp.route('/applications')
@applications_bp.route('/applications/<app_type>')
def get_app(app_type=None):
    test = ["India", "Turkey", "Egypt"]
    filtered_Array = []
    for x in automations_list:
        if x['Country'] == app_type:
            filtered_Array.append(x)
    return render_template('applications.html', categories=test, app_type=app_type, automations=filtered_Array)

@applications_bp.route('/run-automation/<app_name>', methods=['POST', 'GET'])
def set_variables(app_name=None):
    filtered_Array = []
    for x in automations_list:
        if x['Title'] == app_name:
            filtered_Array.append(x)
    requirements = filtered_Array[0]['Requirements']
    if request.method == 'POST': 
        data = request.get_json()
        filtered_Array[0]['Type'](data)
        return 'hello'
    else:
        return render_template('run_automation.html', app_name=app_name, requirements=requirements)
