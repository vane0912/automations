from flask import render_template
from .automations_list import automations_list_weekly
from .applications import check_status
from flask import Blueprint, render_template, request, current_app, jsonify, make_response
from threading import Thread

from flask import Blueprint

weekly_bp = Blueprint('weekly', __name__)

@weekly_bp.route('/weekly')
def weekly():
    check_status.clear()
    return render_template('weekly.html', automations_list=automations_list_weekly)
@weekly_bp.route('/weekly/<title>', methods=['POST'])
def runAutomation(title=None):
    if request.method == 'POST':
        automation = []
        for x in automations_list_weekly:
            if x['Title'] == title:
                automation.append(x)
        def long_running_task(data):
            results = automation[0]['Type'](data['url'], data['email'])
            return results
        thread = Thread(target=long_running_task, args=(request.get_json(),)) 
        thread.start()
        return jsonify({'message': 'Task Started'})