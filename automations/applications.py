import asyncio
from .automations_list import automations_list
from flask import Blueprint, render_template, request, current_app, jsonify, Response

applications_bp = Blueprint('applications', __name__)

@applications_bp.route('/applications')
@applications_bp.route('/applications/<app_type>')

def get_app(app_type=None):
    categories = []
    filtered_Array = []
    for x in automations_list:
        if x['Country'] == app_type or x['Enabled'] == True:
            categories.append(x['Country'])
            filtered_Array.append(x)
    return render_template('applications.html', categories=categories, app_type=app_type, automations=filtered_Array)

@applications_bp.route('/run-automation/<app_name>', methods=['POST', 'GET'])
def set_variables(app_name=None):
    url=''
    if current_app.config['ENVIROMENT_VARIABLE'] == 'production':
        url = current_app.config['URL_VARIABLE']
    else: 
        url = 'http://127.0.0.1:5000'
    filtered_Array = []
    for x in automations_list:
        if x['Title'] == app_name:
            filtered_Array.append(x)
    status = []
    requirements = filtered_Array[0]['Requirements']
    for x in requirements:
        if x['Label'] == 'Status':
            status.append(x)
    if request.method == 'POST': 
        data = request.get_json()
        try:
            results = filtered_Array[0]['Type'](data)
            return jsonify(results)
        except Exception as e:
            print(Exception)
            return jsonify({'error': str(e)})
    else:
        return render_template('run_automation.html', app_name=app_name, requirements=requirements, status=status[0]['Status_Available'], goto=url)
