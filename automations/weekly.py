from flask import render_template
from .automations_list import automations_list_admin
from .applications import check_status
from flask import Blueprint, render_template, request, current_app, jsonify, make_response
from threading import Thread

from flask import Blueprint

admin = Blueprint('admin', __name__)

@admin.route('/admin')
def weekly():
    check_status.clear()
    automations_enabled = [item for item in automations_list_admin if item['Enabled']]
    return render_template('admin.html', automations_list=automations_enabled)
@admin.route('/admin/<title>', methods=['POST'])
def runAutomation(title=None):
    if request.method == 'POST':
        automation = []
        for x in automations_list_admin:
            if x['Title'] == title:
                automation.append(x)
        def long_running_task(data):
            results = automation[0]['Type'](data['url'])
            return results
        thread = Thread(target=long_running_task, args=(request.get_json(),)) 
        thread.start()
        return jsonify({'message': 'Task Started'})