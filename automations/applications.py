import json
from .automations_list import automations_list
from flask import Blueprint, render_template, request, current_app, jsonify, make_response

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
async def set_variables(app_name=None):
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
            send_success = make_response(render_template('run_automation.html',app_name=app_name, requirements=requirements, status=status[0]['Status_Available'], goto=url))
            send_success.set_cookie('Status', json.dumps(results))
            return send_success
        except Exception as e:
            send_failed = make_response(render_template('run_automation.html',app_name=app_name, requirements=requirements, status=status[0]['Status_Available'], goto=url))
            send_failed.set_cookie('Status', 'Failed')
            send_failed.set_cookie('error', str(e))
            return send_failed
    else:
        response = make_response(render_template('run_automation.html',app_name=app_name, requirements=requirements, status=status[0]['Status_Available'], goto=url))   
        response.set_cookie('Status', '')
        response.set_cookie('error', '')
        return response
@applications_bp.route('/check-automation-status')
def check_automation_status():
    try:
        get_response_cookie = request.cookies.get('Status')
        if len(get_response_cookie) > 0:
            if get_response_cookie == 'Failed':
                status = request.cookies.get('Status')
                error = request.cookies.get('error')
                check_status = {
                    'status': status,
                    'errorMsg': error
                }
            else:
                cookie_dict = json.loads(get_response_cookie)
                order_numbers = cookie_dict.get('Order_numbers')
                status = cookie_dict.get('Status')
                email = cookie_dict.get('email')
                order_status = cookie_dict.get('order_status')
                check_status = {
                    'status': status,
                    'results': order_numbers,
                    'email': email,
                    'order_status': order_status
                }
        else:
            check_status = {
                'status': '',
                'results': []
            }
        return jsonify(check_status)
    
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return jsonify({'error': str(e)})