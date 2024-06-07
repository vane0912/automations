from .automations_list import automations_list
from flask import Blueprint, render_template

# Define a blueprint for your applications
applications_bp = Blueprint('applications', __name__)

@applications_bp.route('/applications')
@applications_bp.route('/applications/<app_type>')
def runapp(app_type=None):
    test = ["India", "Turkey", "Egypt"]
    filtered_Array = []
    for x in automations_list:
        if x['Country'] == app_type:
            filtered_Array.append(x)
    return render_template('applications.html', categories=test, app_type=app_type, automations=filtered_Array)

@applications_bp.route('/test', methods=['POST'])
def testrun():
    return 'this worked'
